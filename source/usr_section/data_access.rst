.. include:: /icon_links.rst

.. |reg| unicode:: U+000AE .. REGISTERED SIGN

.. _data_access:

==================
EnMAP Data
==================

.. admonition:: Info

    This section is intended to guide the user through the workflow of downloading their first EnMAP image. The section will cover information about:

    * The EnMAP Instrument Planning Portal (IPP)
    * The EOWEB |reg| GeoPortal (EGP)
    * Download the data from the FTP server

    For a more detailed description take a look at the `Portal User Manual <https://www.enmap.org/data/doc/EN-GS-UM-6020_Portals_User_Manual_v1.4.pdf>`_.

EnMAP Data Access Portal
========================

The EnMAP Data Access Portal (EDAP) includes two major entry points:

    * the EnMAP Instrument Planning Portal (IPP)
    * the EOWEB |reg| GeoPortal (EGP)

To access the EnMAP image archive, a primary registration to the IPP is necessary to be able to access the EOWEB |reg| GeoPortal.

    .. figure:: /img/enmap_dataAccess.png
       :align: center

       Overview of the EnMAP Data Access Portals

Step 1: Instrument Planning Portal (IPP)
----------------------------------------

The IPP enables the user registration, the submission of user proposals, and the planning and submitting of future orders.

    1. Click the :guilabel:`Sign-Up` button to register at the `Instrument Planning Portal landing page <https://planning.enmap.org/>`_.

      .. note:: An e-mail is send to your address containing a verification code.

    2. After the successful registration, login to the Instrument Planning Portal and enter the **User Portal**

        .. figure:: /img/enmap_userPortal.png
           :align: center

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
------------------------

The EOWEB |reg| GeoPortal access link is created for Cat-1 users after the requested role has been approved by the reviewer.
The login button appears on the User Portal page, which automatically directs to the EOWEB |reg| GeoPortal login page.

    .. figure:: /img/enmap_eoweb_login.png
       :align: center

       Entry point to the EOWEB GeoPortal

    1. Login with the respective User ID associated with the approved role request. The password remains the same as when logging into the Instrument Planning Portal.
    2. Once logged in, click :guilabel:`Show advanced map` to zoom, pan and draw a rectangle.
    3. Select :file:`EnMAP` in *Filter Collection* and confirm with :guilabel:`Search`.

        .. note:: You may also want to check the :guilabel:`EnMAP-HSI (LO), Low Quality` box to see additional records that are marked as low quality, but are still good.

    4. Hide :guilabel:`Show advanced map` to see the results.

        .. figure:: /img/enmap_eowebPortal.png
           :align: center

    5. Place your order and wait until you get notified.

Step 3: Download data from the FTP Delivery Server
------------------------------------------------

After the order is placed, an e-mail is sent including a link to the FTP server and the zipped data.

.. note:: The User ID and password to access the FTP server are identical to the EOWEB |reg| GeoPortal credentials.

To download the data use a FTP client, for example FileZilla. For further help on how to download the data from the FTP server take
a look at `Downloading Ordered Data <https://eoweb.dlr.de/egp/docs/user/downloading_ordered_data.html>`_.

    .. figure:: /img/enmap_downloadData.png
       :align: center

       Example of FTPS settings in FileZilla
