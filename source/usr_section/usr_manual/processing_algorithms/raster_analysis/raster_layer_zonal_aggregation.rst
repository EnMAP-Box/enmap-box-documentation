.. _Raster layer zonal aggregation:

******************************
Raster layer zonal aggregation
******************************

Aggregates `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ `pixel profiles <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pixel-profile>`_ by `categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_.

.. include:: ../../processing_algorithms_includes/raster_analysis/raster_layer_zonal_aggregation.rst

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be aggregated.


:guilabel:`Categorized raster layer` [raster]
    `Categorized raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-raster-layer>`_ specifying the zones.

**Outputs**


:guilabel:`Output table` [vectorDestination]
    `Table <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-table>`_ file destination.

**Command-line usage**

``>qgis_process help enmapbox:RasterLayerZonalAggregation``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    categorizedRaster: Categorized raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    outputTable: Output table
    	Argument type:	vectorDestination
    	Acceptable values:
    		- Path for new vector layer
    
    ----------------
    Outputs
    ----------------
    
    outputTable: <outputVector>
    	Output table
    
    