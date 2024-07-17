.. include:: /icon_links.rst

Metadata Guide
**************

The metadata guide explains how the EnMAP-Box uses raster metadata.
In general, metadata is used to annotate the actual raster data with additional information to allow tools and
algorithms to make better use of them.
E.g. we need the center wavelength of each band in an optical image to properly plot spectral profiles,
and we need the acquisition datetime of each band in a temporal raster stack to properly plot temporal profiles.

The EnMAP-Box supports multiple levels of raster metadata specifications.
If a metadata item is requested, we look for it inside the following places and sequential order:

1. Metadata stored inside a STAC ***.stac.json** sidecar file (e.g. *myRaster.bsq.stac.json*).
2. Metadata stored inside a GDAL PAM ***.aux.xml** sidecar file (e.g. *myRaster.bsq.aux.xml*).
3. Metadata stored inside a GDAL source file (e.g. *myRaster.hdr*).

Note that metadata items can be specified in multiple places, with potentially conflicting values.
It is the responsibility of the user, to make sure, that lower-level metadata
(e.g. metadata inside an ENVI *.hdr* header file), isn't shadowed by higher-level specifications (e.g. GDAL PAM or STAC).

Introduction to STAC Metadata
=============================

The EnMAP-Box supports metadata stored inside a STAC (SpatioTemporal Asset Catalogs) ***.stac.json** sidecar file.
See the STAC specification for more details: https://stacspec.org/en

Currently we use the `Electro-Optical Extension Specification <https://github.com/stac-extensions/eo>`_  and
the `Timestamps Extension Specification <https://github.com/stac-extensions/timestamps>`_ for describing most of the
spectral, temporal and general metadata items.

For special metadata items, not already covered by an official STAC extensions, we introduce new items with our custom
**enmapbox:** field name prefix, e.g. **enmapbox:bad_band_multiplier**

For a hyperspectral raster, the STAC metadata looks like this::

    {
      "stac_extensions": [
        "https://stac-extensions.github.io/eo/v1.0.0/schema.json",         # Electro-Optical Extension Specification: https://github.com/stac-extensions/eo
        "https://stac-extensions.github.io/timestamps/v1.1.0/schema.json"  # Timestamps Extension Specification: https://github.com/stac-extensions/timestamps
      ],
      "properties": {
        "datetime": "2022-07-24T10:45:26",         # Scene acquisition datetime",
        "eo:bands": [                              # List of band-specific metadata items
          {                                        #   First band
            "name": "band 1 (418.24 Nanometers)",  #     Band name (used by tools/algorithms, but not displayed by QGIS!)
            "center_wavelength": 0.41824,          #     Center wavelength in micrometers
            "full_width_half_max": 0.00699561,     #     Full width at half maximum in micrometers
            "enmapbox:bad_band_multiplier": 1      #     Whether a band is a good band (1) or a bad band (0)
          },
          {                                        #   Second band
            "name": "band 2 (423.874 Nanometers)",
            "center_wavelength": 0.423874,
            "full_width_half_max": 0.006667,
            "enmapbox:bad_band_multiplier": 1
          },
          ... ,
          {                                        #   Last band
            "name": "band 224 (2445.53 Nanometers)",
            "center_wavelength": 2.44553,
            "full_width_half_max": 0.0071581,
            "enmapbox:bad_band_multiplier": 1
          }
        ]
      }
    }

For a 3D temporal band stack (e.g. NDVI bands over time), the STAC metadata looks like this::

    {
      "properties": {
        "eo:bands": [                              # List of band-specific metadata items
          {                                        #   First band
            "name": "NDVI (2022-07-24)",
            "datetime": "2022-07-24T10:45:26"
          },
          {                                        #   Second band
            "name": "NDVI (2022-08-05)",
            "datetime": "2022-08-05T10:42:12"
          },
          ... ,
        ]
      }
    }

For a 4D temporal band stack with multiple variables over time (e.g. NDVI, EVI bands), the STAC metadata looks like this::

    {
      "properties": {
        "eo:bands": [                              # List of band-specific metadata items
          {                                        #   First band (first variable, first date)
            "name": "NDVI (2022-07-24)",
            "datetime": "2022-07-24T10:45:26"
          },
          {                                        #   Second band (second variable, first date)
            "name": "EVI (2022-07-24)",
            "datetime": "2022-07-24T10:45:26"
          },
          {                                        #   Third band (first variable, second date)
            "name": "NDVI (2022-08-05)",
            "datetime": "2022-08-05T10:42:12"
          },
          {                                        #   Fourth band (second variable, second date)
            "name": "EVI (2022-08-05)",
            "datetime": "2022-08-05T10:42:12"
          },
          ... ,
        ]
      }
    }

If the temporal data represents an aggregation of multiple observations inside a temporal range
(e.g. cloud-free composites for individual years), use the `start_datetime` and `end_datetime` keys,
instead of `datetime`::

   {
     "properties": {
       "eo:bands": [
         {
           "name": "NDVI 2022",
           "start_datetime": "2022-01-01T00:00:00",
           "end_datetime": "2023-01-01T00:00:00"
         },
         ... ,
       ]
     }
   }

In case of a 4D spectral-temporal band stack (e.g. yearly Landsat composites over time), use spectral and temporal
metadata together, to fully describe the dataset::

   {
     "properties": {
       "eo:bands": [
         {
           "name": "Blue (450-520 Nanometers) - 2022",
           "start_datetime": "2022-01-01T00:00:00",
           "end_datetime": "2023-01-01T00:00:00",
           "center_wavelength": 0.456
         },
         ... ,
       ]
     }
    }

As an alternative to the above described specifications, we also support a more concise ENVI-like specification,
using the well known `ENVI Header File <https://www.nv5geospatialsoftware.com/docs/enviheaderfiles.html#The>`_
metadata items. This should allow for simple copy&paste approaches,
when moving metadata from an ENVI Header file to a STAC file::

   {
     "properties": {
       "envi:metadata": {
         "band_names": ["band 1 (418.24 Nanometers)", "band 2 (423.874 Nanometers)", ..., band 224 (2445.53 Nanometers)],
         "wavelength": [418.24, 423.874, ..., 2445.53],
         "wavelength_units": "Nanometers",
         "fwhm": [6.99561, 6.667, ..., 7.1581],
         "bbl": [1, 1, ..., 1],
         "acquisition_time": "2022-01-01T12:00:00"
       }
    }

To fully support temporal raster stacks with ENVI-Style specification, we also check for "eo:" items. E.g.::

   {
     "properties": {
       "envi:metadata": {
         "eo:datetime": ["2022-07-24T10:45:26", "2022-08-05T10:42:12", ...]
       }
    }

Or::

   {
     "properties": {
       "envi:metadata": {
         "eo:start_datetime": ["2021-01-01T00:00:00", "2022-01-01T00:00:00", ...]
         "eo:end_datetime": ["2022-01-01T00:00:00", "2023-01-01T00:00:00", ...]
       }
    }


Introduction to GDAL Metadata
=============================

The EnMAP-Box supports metadata stored inside a GDAL PAM (Persistent Auxiliary Metadata) ***.aux.xml** sidecar file.

For a hyperspectral raster, the GDAL PAM metadata looks like this::

    <PAMDataset>
      <PAMRasterBand band="1">                                    # First band
        <Description>band 8 (0.460000 Micrometers)</Description>  #   Band name
        <Metadata>
          <MDI key="wavelength">0.460000</MDI>                    #   Center wavelength
          <MDI key="fwhm">0.058</MDI>                             #   Full width at half maximum
          <MDI key="wavelength_units">Micrometers</MDI>           #   Wavelength units
          <MDI key="bbl">1</MDI>                                  #   Whether a band is a good band (1) or a bad band (0)
        </Metadata>
      </PAMRasterBand>

      <PAMRasterBand band="2">                                    # Second band
        ...
      </PAMRasterBand>

      ...

    </PAMDataset>

For a 3D temporal band stack (e.g. NDVI bands over time), the GDAL PAM metadata looks like this::

    <PAMDataset>
      <PAMRasterBand band="1">                                    # First band
        <Description>NDVI (2022-07-24)</Description>
        <Metadata>
          <MDI key="start_time">2022-07-24T10:45:26</MDI>
        </Metadata>
      </PAMRasterBand>

      <PAMRasterBand band="2">                                    # Second band
        <Description>NDVI (2022-08-05)</Description>
        <Metadata>
          <MDI key="start_time">2022-08-05T10:42:12</MDI>
        </Metadata>
      </PAMRasterBand>

      ...

    </PAMDataset>

For a 4D temporal band stack with multiple variables over time (e.g. NDVI, EVI bands), the GDAL PAM metadata looks like this::

    <PAMDataset>
      <PAMRasterBand band="1">                                    # First band (first variable, first date)
        <Description>NDVI (2022-07-24)</Description>
        <Metadata>
          <MDI key="start_time">2022-07-24T10:45:26</MDI>
        </Metadata>
      </PAMRasterBand>


      <PAMRasterBand band="2">                                    # Second band (second variable, first date)
        <Description>EVI (2022-07-24)</Description>
        <Metadata>
          <MDI key="start_time">2022-07-24T10:45:26</MDI>
        </Metadata>
      </PAMRasterBand>

      <PAMRasterBand band="3">                                    # Third band (first variable, second date)
        <Description>NDVI (2022-08-05)</Description>
        <Metadata>
          <MDI key="start_time">2022-08-05T10:42:12</MDI>
        </Metadata>
      </PAMRasterBand>

      <PAMRasterBand band="4">                                    # Fourth band (second variable, second date)
        <Description>EVI (2022-08-05)</Description>
        <Metadata>
          <MDI key="start_time">2022-08-05T10:42:12</MDI>
        </Metadata>
      </PAMRasterBand>

      ...

    </PAMDataset>

If the temporal data represents an aggregation of multiple observations inside a temporal range
(e.g. cloud-free composites for individual years), use the `start_datetime` and `end_datetime` keys,
instead of `datetime`::

    <PAMDataset>
      <PAMRasterBand band="1">
        <Description>NDVI 2022</Description>
        <Metadata>
          <MDI key="start_time">2022-01-01T00:00:00</MDI>
          <MDI key="end_time">2023-01-01T00:00:00</MDI>
        </Metadata>
      </PAMRasterBand>

      ...

    </PAMDataset>

In case of a 4D spectral-temporal band stack (e.g. yearly Landsat composites over time), use spectral and temporal
metadata together, to fully describe the dataset::

    <PAMDataset>
      <PAMRasterBand band="1">
        <Description>Blue (450-520 Nanometers) - 2022</Description>
        <Metadata>
          <MDI key="start_time">2022-01-01T00:00:00</MDI>
          <MDI key="end_time">2023-01-01T00:00:00</MDI>
          <MDI key="wavelength">0.456</MDI>
          <MDI key="wavelength_units">Micrometers</MDI>
        </Metadata>
      </PAMRasterBand>

      ...

    </PAMDataset>

As an alternative to the above described specifications, we also support a more concise ENVI-like specification,
using the well known `ENVI Header File <https://www.nv5geospatialsoftware.com/docs/enviheaderfiles.html#The>`_
metadata items. This should allow for simple copy&paste approaches,
when moving metadata from an ENVI Header file to a GDAL PAM file::

    <PAMDataset>
      <Metadata domain="ENVI">
        <MDI key="wavelength">{418.24, 423.874, ..., 2445.53}</MDI>
        <MDI key="fwhm">{6.99561, 6.667, ..., 7.1581}</MDI>
        <MDI key="wavelength_units">Nanometers</MDI>
        <MDI key="bbl">{ 1, 1, ..., 1}
        ...
      </Metadata>
      <PAMRasterBand band="1">
        <Description>band 1 (418.24 Nanometers)</Description>
      </PAMRasterBand>

      <PAMRasterBand band="2">
        <Description>band 2 (423.874 Nanometers)</Description>
      </PAMRasterBand>

      ...

      <PAMRasterBand band="224">
        <Description>band 224 (2445.53 Nanometers)</Description>
      </PAMRasterBand>

    </PAMDataset>
