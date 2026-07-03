.. _data_access:

===========
Data Access
===========

DLR Geoservice
--------------

The DLR Earth Observation Center (EOC) Geoservice provides programmatic and immediate access to Earth Observation datasets, including EnMAP Hyperspectral Imagery (HSI), without the need for manual downloading through the web portal.


To access and download EnMAP data, you must have a registered account.

1. Navigate to the EnMAP Instrument Planning Portal or the EOWEB |reg| GeoPortal.
2. Click on :guilabel:`Registration` or :guilabel:`Sign-up`.

.. important::
   Under current EnMAP data policies, you must register using an **institutional or company email address** (e.g., affiliated with a university, research center, or commercial enterprise). If you do not have an institutional email address, you must apply for a special exemption by writing directly to ``enmap_registration@dlr.de``.

3. Fill out your affiliation details and accept the EnMAP Data License Agreement.

Search and Download with QGIS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. hint::

    QGIS has native STAC support since version 3.40. However, as now (2026-05-31), it does not allow to use
    STAC authentification differing between *search* and *download* (`QGIS issue #60752 <https://github.com/qgis/QGIS/issues/60752#issuecomment-4442747402>`_).

    To download EOC Geoservice STAC assets in QGIS, you need to provide your user credentials using the GDAL_HTTP_USERPWD environmental variable.

1. Set the environmental variables GDAL_HTTP_AUTH and GDAL_HTTP_USERPWD

   .. code-block:: bash

        GDAL_HTTP_AUTH=BASIC
        GDAL_HTTP_USERPWD=<your Geoservice user name>:<your Geoservice password>

   E.g. open *Settings* > *Options*, select the *System* panel, go to *Environment*, define the missing environmental variables and restart QGIS

   .. figure:: img/stac_dlr_gdalvariables.png


2. Open QGIS and zoom to your region of interest, e.g. "New Delhi". Then open *Layer* > *Add Layer* > *Add Layer from STAC Catalog ...*

   .. figure:: img/stac_newdelhi.png

3. Now add the DLR EOC Geoservice (`https://geoservice.dlr.de/eoc/ogc/stac/v1/ <https://geoservice.dlr.de/eoc/ogc/stac/v1/>`_)as STAC connection

   .. figure:: img/stac_connection_details.png

4. Edit *Filter...*. Set the spatial extent to the current map extent / any other region of interest and search for EnMAP L2A HSI Products only

   .. figure:: img/stac_filters.png

5. Wait until the search results are returned. Click on a result to see its spatial extent in the QGIS map.
   Use the context menu to download STAC assets.

   .. figure:: img/stac_filter_selection.png

..
    3. Searching for EnMAP HSI Data (Example: New Delhi)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Once connected, you can query specific collections using a spatial subset. Here is how to find EnMAP Level 2A data over New Delhi:

    1. Expand the new **DLR EOC Geoservice** connection in your Browser Panel.
    2. Expand the **Collections** folder.
    3. Scroll down to find ``EnMAP HSI - Level 2A Hyperspectral Images - Global``.
    4. Right-click it and select **Open in Data Source Manager** (or simply double-click).
    5. In the Data Source Manager, apply a **Spatial Filter** (Bounding Box) to search for your Area of Interest (e.g. New Delhi). Enter the following coordinates:

       * **West:** ``76.83``
       * **South:** ``28.40``
       * **East:** ``77.34``
       * **North:** ``28.88``

    6. Click :guilabel:`Filter/Search`.
    7. Drag and drop the resulting COG (Cloud-Optimized GeoTIFF) assets directly onto your QGIS map canvas to load the hyperspectral imagery.

    .. figure:: /img/placeholder_search.gif
       :align: center
       :width: 90%

       Searching for New Delhi EnMAP Data via Data Source Manager

EODAG
^^^^^
The `Earth Observation Data Access Gateway (EODAG) <https://eodag.readthedocs.io>`_ provides unified programmatic access to different Earth Observation data providers. You can use EODAG via Python to automatically search and download EnMAP Analysis Ready Data (Level-2A) directly from the DLR EOC Geoservice.

.. note::
   Ensure you are using an up-to-date version of EODAG (``pip install --upgrade eodag``), as native support for the DLR Geoservice was added in recent releases.

1. Configure DLR Credentials
****************************

To access EnMAP data via EODAG, you must configure it to use your DLR Geoservice credentials (the same account you use for the EOWEB® GeoPortal).

Add the ``dlr_eoc_geoservice`` provider to your EODAG configuration file. By default, this file is located at ``~/.config/eodag/eodag.yml`` on Linux/macOS or ``%USERPROFILE%\.config\eodag\eodag.yml`` on Windows.

.. code-block:: yaml

    dlr_eoc_geoservice:
      auth:
        credentials:
          username: "YOUR_EOWEB_USERNAME"
          password: "YOUR_EOWEB_PASSWORD"

2. Search and Download via Python
*********************************

Once configured, use the EODAG Python API to query the ``ENMAP_HSI_L2A`` collection. The following script searches for EnMAP scenes over a specific bounding box and downloads them to a local directory.

.. code-block:: python

    import os
    from eodag import EODataAccessGateway

    # Initialize EODAG and prioritize the DLR Geoservice
    dag = EODataAccessGateway()
    dag.set_preferred_provider("dlr_eoc_geoservice")

    # Define your search parameters
    search_criteria = {
        "collection": "ENMAP_HSI_L2A",
        "geom": {"lonmin": 13.0, "latmin": 52.0, "lonmax": 13.5, "latmax": 52.5}, # Example: Berlin area bounding box
        "start": "2023-05-01",
        "end": "2023-09-30"
    }

    print("Searching DLR Geoservice for EnMAP products...")
    search_results = dag.search(**search_criteria)
    print(f"Found {len(search_results)} products.")

    # Define where to save the files
    download_dir = os.path.join(os.getcwd(), "enmap_downloads")
    os.makedirs(download_dir, exist_ok=True)

    # Download and automatically extract the products
    print("Downloading products...")
    downloaded_paths = dag.download_all(
        search_results,
        outputs_prefix=download_dir,
        extract=True
    )

    print(f"Download complete. Files saved to: {download_dir}")

After the download and extraction finish, you can load the resulting imagery directly into QGIS by dragging the files into the EnMAP-Box **Data Views** panel.

Troubleshooting
^^^^^^^^^^^^^^^

Because the Geoservice provides direct access to live institutional servers, you may occasionally experience connection timeouts.

.. note::
   **Encountering a "Bad Gateway" (HTTP 502) Error?**
   This indicates that your QGIS connection is configured perfectly, but the DLR server is temporarily undergoing maintenance or experiencing heavy load. If this occurs, verify your URL is correct, wait a short while, and try expanding the folder again.

EnMAP Data Access Portal
------------------------

.. admonition:: Info

    This section is intended to guide the user through the workflow of downloading their first EnMAP image. The section will cover information about:

    * The EnMAP Instrument Planning Portal (IPP)
    * The EOWEB |reg| GeoPortal (EGP)
    * Download the data from the FTP server

    For a more detailed description take a look at the `Portal User Manual <https://www.enmap.org/data/doc/EN-GS-UM-6020_Portals_User_Manual_v1.4.pdf>`_.


The EnMAP Data Access Portal (EDAP) includes two major entry points:

    * the EnMAP Instrument Planning Portal (IPP)
    * the EOWEB |reg| GeoPortal (EGP)

To access the EnMAP image archive, a primary registration to the IPP is necessary to be able to access the EOWEB |reg| GeoPortal.

    .. figure:: /img/enmap_dataAccess.png
       :align: center
       :width: 100%

       Overview of the EnMAP Data Access Portals

Step 1: Instrument Planning Portal (IPP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IPP enables the user registration, the submission of user proposals, and the planning and submitting of future orders.

    1. Click the :guilabel:`Sign-Up` button to register at the `Instrument Planning Portal landing page <https://planning.enmap.org/>`_.

      .. note:: An e-mail is send to your address containing a verification code.

    2. After the successful registration, login to the Instrument Planning Portal and enter the **User Portal**

        .. figure:: /img/enmap_userPortal.png
           :align: center
           :width: 100%

    3. In the User Portal, the user has to go through the *Role Assignment* procedure which is used to assign different priorities to observation requests.
       For more information about the different *User Roles* please take a look at the `Portal User Manual <https://www.enmap.org/data/doc/EN-GS-UM-6020_Portals_User_Manual_v1.4.pdf>`_.

        * To access the data archive, request **Catalogue (Cat1-Distributor)**
        * To request data takes / submit proposals for data takes, request **Cat-1**


        .. figure:: /img/enmap_userRoles.png
           :align: center
           :width: 800

    4. Wait until the respective role is assigned. Note: This will take a few hours.
    5. Once the role has been assigned, a new box will appear in the User Portal, allowing you tp access the EOWEB |reg| GeoPortal to search the EnMAP Data archive and order images.

Step 2: EOWEB |reg| GeoPortal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The EOWEB |reg| GeoPortal access link is created for Cat-1 users after the requested role has been approved by the reviewer.
The login button appears on the User Portal page, which automatically directs to the EOWEB |reg| GeoPortal login page.

    .. figure:: /img/enmap_eoweb_login.png
       :align: center
       :width: 100%

       Entry point to the EOWEB GeoPortal

    1. Login with the respective User ID associated with the approved role request. The password remains the same as when logging into the Instrument Planning Portal.
    2. Once logged in, click :guilabel:`Show advanced map` to zoom, pan and draw a rectangle.
    3. Select :file:`EnMAP` in *Filter Collection* and confirm with :guilabel:`Search`.

        .. note:: You may also want to check the :guilabel:`EnMAP-HSI (LO), Low Quality` box to see additional records that are marked as low quality, but are still good.

    4. Hide :guilabel:`Show advanced map` to see the results.

        .. figure:: /img/enmap_eowebPortal.png
           :align: center
           :width: 100%

    5. Place your order and wait until you get notified.

Step 3: Download data from the FTP Delivery Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After the order is placed, an e-mail is sent including a link to the FTP server and the zipped data.

.. note:: The User ID and password to access the FTP server are identical to the EOWEB |reg| GeoPortal credentials.

To download the data use a FTP client, for example FileZilla. For further help on how to download the data from the FTP server take
a look at `Downloading Ordered Data <https://eoweb.dlr.de/egp/docs/user/downloading_ordered_data.html>`_.

    .. figure:: /img/enmap_downloadData.png
       :align: center
       :width: 60%

       Example of FTPS settings in FileZill


.. AUTOGENERATED SUBSTITUTIONS - DO NOT EDIT PAST THIS LINE

.. |reg| unicode:: U+000AE .. REGISTERED SIGN
    :ltrim:
