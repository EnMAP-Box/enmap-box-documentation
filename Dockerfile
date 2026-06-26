# syntax=docker/dockerfile:1

ARG UBUNTU_VERSION=24.04
ARG TARGETPLATFORM=linux/amd64

FROM python:3.12-slim AS docs

WORKDIR /docs

RUN apt-get update \
    && apt-get install -y --no-install-recommends make \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["make", "html"]


# QGIS packages from qgis.org are published for amd64. Pin the image platform
# so this target can also be built from Apple Silicon hosts via Docker emulation.
FROM --platform=${TARGETPLATFORM} ubuntu:${UBUNTU_VERSION} AS qgis-enmapbox-base

ARG DEBIAN_FRONTEND=noninteractive
ARG QGIS_REPOSITORY=https://qgis.org/ubuntu-ltr
ARG QGIS_SUITE=noble
ARG QGIS_PLUGIN_QGIS_VERSION=3.44
ARG ENMAPBOX_REQUIREMENTS_URL=https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/linux/requirements_ubuntu.txt
ARG ENMAPBOX_PLUGIN_NAME="EnMAP-Box 3"
ARG ENMAPBOX_PLUGIN_ID=enmapboxplugin
ARG ENMAPBOX_USER=enmapbox
ARG ENMAPBOX_UID=1000
ARG ENMAPBOX_GID=1000

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       gnupg \
       wget \
    && install -d -m 0755 /etc/apt/keyrings \
    && wget -qO /etc/apt/keyrings/qgis-archive-keyring.gpg \
       https://download.qgis.org/downloads/qgis-archive-keyring.gpg \
    && printf 'Types: deb deb-src\nURIs: %s\nSuites: %s\nArchitectures: amd64\nComponents: main\nSigned-By: /etc/apt/keyrings/qgis-archive-keyring.gpg\n' \
       "${QGIS_REPOSITORY}" "${QGIS_SUITE}" > /etc/apt/sources.list.d/qgis.sources \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       dbus-x11 \
       libgl1 \
       make \
       pyqt5-dev-tools \
       python3-dev \
       python3-h5py \
       python3-matplotlib \
       python3-netcdf4 \
       python3-pip \
       python3-pyqt5.qtopengl \
       python3-qgis \
       python3-venv \
       qgis \
       qgis-plugin-grass \
       unzip \
       xauth \
       xvfb \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --no-cache-dir --break-system-packages --ignore-installed \
       -r "${ENMAPBOX_REQUIREMENTS_URL}" \
       qgis-plugin-manager && \
    python3 -m pip install --no-cache-dir --break-system-packages --force-reinstall \
        "numpy==1.26.4" \
        "scipy==1.14.1" \
        "scikit-learn==1.5.2"

RUN set -eux; \
    if getent group "${ENMAPBOX_GID}" >/dev/null; then \
        ENMAPBOX_GROUP="$(getent group "${ENMAPBOX_GID}" | cut -d: -f1)"; \
    else \
        groupadd --gid "${ENMAPBOX_GID}" "${ENMAPBOX_USER}"; \
        ENMAPBOX_GROUP="${ENMAPBOX_USER}"; \
    fi; \
    if id -u "${ENMAPBOX_USER}" >/dev/null 2>&1; then \
        usermod --gid "${ENMAPBOX_GROUP}" "${ENMAPBOX_USER}"; \
        usermod --uid "${ENMAPBOX_UID}" "${ENMAPBOX_USER}"; \
    elif getent passwd "${ENMAPBOX_UID}" >/dev/null; then \
        EXISTING_USER="$(getent passwd "${ENMAPBOX_UID}" | cut -d: -f1)"; \
        usermod --login "${ENMAPBOX_USER}" --home "/home/${ENMAPBOX_USER}" --move-home "${EXISTING_USER}"; \
        usermod --gid "${ENMAPBOX_GROUP}" "${ENMAPBOX_USER}"; \
    else \
        useradd --uid "${ENMAPBOX_UID}" --gid "${ENMAPBOX_GROUP}" \
            --create-home --shell /bin/bash "${ENMAPBOX_USER}"; \
    fi; \
    mkdir -p "/home/${ENMAPBOX_USER}"; \
    chown -R "${ENMAPBOX_UID}:${ENMAPBOX_GID}" "/home/${ENMAPBOX_USER}"

COPY docker/qgis-enmapbox-entrypoint.sh /usr/local/bin/qgis-enmapbox-entrypoint
RUN chmod 0755 /usr/local/bin/qgis-enmapbox-entrypoint

USER ${ENMAPBOX_USER}
WORKDIR /home/${ENMAPBOX_USER}

ENV HOME=/home/${ENMAPBOX_USER}
ENV QGIS_PROFILE=EnMAP-Box
ENV QGIS_PROFILE_HOME=${HOME}/.local/share/QGIS/QGIS3/profiles/${QGIS_PROFILE}
ENV QGIS_PLUGINPATH=${QGIS_PROFILE_HOME}/python/plugins
ENV PYTHONPATH=/usr/share/qgis/python/plugins:${QGIS_PLUGINPATH}/enmapboxplugin
ENV QGIS_PLUGIN_MANAGER_SOURCES_FILE=${QGIS_PROFILE_HOME}/python/plugins/sources.list
ENV QGIS_PLUGIN_MANAGER_CACHE_DIR=${HOME}/.cache/qgis-plugin-manager
ENV QT_QPA_PLATFORM=offscreen

FROM qgis-enmapbox-base AS qgis-enmapbox

ARG ENMAPBOX_PLUGIN_NAME="EnMAP-Box 3"
ARG QGIS_PLUGIN_QGIS_VERSION=3.44

# Create required directories
RUN mkdir -p "${QGIS_PLUGINPATH}" "${QGIS_PROFILE_HOME}/QGIS" "${QGIS_PLUGIN_MANAGER_CACHE_DIR}"

# Initialize plugin manager with the correct QGIS version
RUN qgis-plugin-manager init --qgis-version "${QGIS_PLUGIN_QGIS_VERSION}"

# Update plugin sources from QGIS repository
RUN qgis-plugin-manager update

# Install the EnMAP-Box plugin
RUN qgis-plugin-manager install "${ENMAPBOX_PLUGIN_NAME}" --upgrade --fix-permissions

# Configure QGIS profile to enable the plugin
RUN printf '[PythonPlugins]\nenmapboxplugin=true\n' \
       | tee "${QGIS_PROFILE_HOME}/QGIS/QGIS.ini" "${QGIS_PROFILE_HOME}/QGIS/QGIS3.ini" > /dev/null

# Verify the plugin installation
RUN test -d "${QGIS_PLUGINPATH}/enmapboxplugin" \
    && python3 -c "from qgis.core import Qgis; print(Qgis.QGIS_VERSION)"

ENTRYPOINT ["qgis-enmapbox-entrypoint"]
CMD ["qgis"]



#Do not use
#qgs.initQgisSettings() -this method does not exist.
#from enmapboxplugin import plugin -this is not the right import for this packaged build.