.. _dev_build_enmapbox_plugin:

Build and publish the EnMAP-Box
###############################


Build the EnMAP-Box Plugin
==========================

Building the EnMAP-Box plugin is done by creating a zip file which the QGIS Plugin Manager
can use to install the EnMAP-Box. This requires that you have setup your development environment
as described in :ref:`the installation for developers <dev_installation>`

Calling:

.. code-block:: bat

    python scripts/create_plugin.py

creates or updates the folder ``deploy`` with:

* the folder ``enmapboxplugin``. It contains the plugin code and additional files
* a file named like ``enmapboxplugin.3.7.20190214T1125.develop.zip``. This is the ``enmapboxplugin``` folder compresses
  as zip file, which can be used by the QGIS Plugin Installer to install the EnMAP-Box.

Using the ``-t`` keyword adds the EnMAP-Box test data, so that you can use and test the EnMAP-Box in QGIS
with having example data already installed.

.. note::

    The ``<subsubversion>`` consists of ``<date>T<time>.<active branch>`` and is generated automatically.

    This helps to generate, test and differentiate between EnMAP-Box versions of different development steps.

A successful build ends with a printout like::

    ### To update/install the EnMAP-Box, run this command on your QGIS Python shell:

    from pyplugin_installer.installer import pluginInstaller
    pluginInstaller.installFromZipFile(r"C:\Users\user\Repositories\QGIS_Plugins\enmap-box\deploy\enmapboxplugin.3.5.20191030T0634.develop.zip")
    #### Close (and restart manually)

    QProcess.startDetached(QgsApplication.arguments()[0], [])
    QgsApplication.quit()

    ## press ENTER

Copy and run it in your QGIS python shell to install the build EnMAP-Box plugin and restart QGIS.
Alternatively, you can install the plugin in QGIS with a few mouse clicks more by:

1. Open the QGIS Plugin Manager
2. Install from ZIP with the created ZIP file
3. Restart QGIS to account for activate changes in python code

Build the EnMAP-Box documentation
=================================

To create the HTML based documentation on your local system call:

.. code-block:: bat

    cd doc
    make html

This creates the folder ``doc/build`` with the HTML documentation. To view the documentation,
just open ``doc/build/html/index.html`` in your webbrowser of choice.


Publish the EnMAP-Box
=====================

Official EnMAP-Box plugin *master* versions are named like ``enmapboxplugin.3.3.20190214T1125.master.zip``. They need to be uploaded
to http://plugins.qgis.org/plugins/ using an OSGeo account.

Other versions, e.g. *development snapshots* are named like ``enmapboxplugin.3.3.20190214T1125.develop.zip`` or ``enmapboxplugin.3.3.20190214T1125.my_feature_branch.zip``
and might be distributed using the repositories download section https://bitbucket.org/hu-geomatics/enmap-box/downloads/.

Updates to the EnMAP-Box documentation (folder ``doc/source``) are detected by readthedocs
when pushed to the *develop* or *master* branch of the EnMAP-Box repository.



