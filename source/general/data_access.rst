.. _data_access:

===========
Data Access
===========

DLR Geoservice
--------------

The DLR Earth Observation Center (EOC) Geoservice provides programmatic and immediate access to Earth Observation datasets, including EnMAP Hyperspectral Imagery (HSI), without the need for manual downloading through the web portal.

1. Registering for DLR Geoservice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To access and download EnMAP data, you must have a registered account.

1. Navigate to the EnMAP Instrument Planning Portal or the EOWEB |reg| GeoPortal.
2. Click on :guilabel:`Registration` or :guilabel:`Sign-up`.

.. important::
   Under current EnMAP data policies, you must register using an **institutional or company email address** (e.g., affiliated with a university, research center, or commercial enterprise). If you do not have an institutional email address, you must apply for a special exemption by writing directly to ``enmap_registration@dlr.de``.

3. Fill out your affiliation details and accept the EnMAP Data License Agreement.

2. Connecting from QGIS with Native STAC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can access the DLR Geoservice directly within QGIS using its native SpatioTemporal Asset Catalog (STAC) support. This is the most stable method for connecting to OGC-compliant APIs.

.. tip::
   **Pro Tip:** While older workflows relied on the external ``qgis_stac`` plugin, QGIS 3.40+ includes native STAC support directly in the Browser Panel. Using this native integration avoids plugin dependency conflicts and is highly recommended!

1. Open QGIS and locate the **Browser Panel** on the left side of your screen.
2. Scroll down until you see the **STAC** icon.
3. Right-click on **STAC** and select **New STAC Connection**.
4. Enter the following connection details:

   * **Name:** ``DLR EOC Geoservice``
   * **URL:** ``https://geoservice.dlr.de/eoc/ogc/stac/v1/``

5. Click :guilabel:`OK`.

.. figure:: /img/STAC_conn_dialog.png
   :align: center
   :width: 80%

   QGIS STAC Connection Setup Dialog

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
