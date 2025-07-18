
..
  ## AUTOGENERATED TITLE START

.. _alg-enmapbox-SpatialConvolutionTrapezoidFilter:

************************************
Spatial convolution Trapezoid filter
************************************

..
  ## AUTOGENERATED TITLE END

..
  ## AUTOGENERATED DESCRIPTION START

2D Trapezoid filter.

..
  ## AUTOGENERATED DESCRIPTION END

The 2D Trapezoid filter uses a trapezoidal weighting function. Thus, the filter assigns higher weights to pixels within a certain range and lower weights to pixels outside that range. It can be used to emphasize or suppress certain features in an image within a specific range of values. The trapezoidal shape of the weighting function allows for a controlled transition of the filter’s effect, enabling customization of the filtering operation based on the desired outcome. An exemplary kernel can be found below.

    .. figure:: ../../processing_algorithms/convolution__morphology_and_filtering/img/trapez_kernel.png
       :align: center

Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms/convolution__morphology_and_filtering/img/trapez_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ../../processing_algorithms/convolution__morphology_and_filtering/img/trapez_filter_result.png
       :align: center

..
  ## AUTOGENERATED PARAMETERS START

**Parameters**

:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be filtered.

:guilabel:`Kernel` [string]
    Python code. See `TrapezoidDisk2DKernel <http://docs.astropy.org/en/stable/api/astropy.convolution.TrapezoidDisk2DKernel.html>`_ for information on different parameters.
    Default::

        from astropy.convolution import TrapezoidDisk2DKernel
        kernel = TrapezoidDisk2DKernel\(radius=3, slope=1\)

:guilabel:`Normalize kernel` [boolean]
    Whether to normalize the kernel to have a sum of one.
    Default: *False*

:guilabel:`Interpolate no data pixel` [boolean]
    Whether to interpolate no data pixel. Will result in renormalization of the kernel at each position ignoring pixels with `no data values <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-no-data-value>`_.
    Default: *True*

**Outputs**

:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

..
  ## AUTOGENERATED PARAMETERS END

..
  ## AUTOGENERATED COMMAND USAGE START

**Command-line usage**

``>qgis_process help enmapbox:SpatialConvolutionTrapezoidFilter``::

    ----------------
    Arguments
    ----------------

    raster: Raster layer
        Argument type:    raster
        Acceptable values:
            - Path to a raster layer
    kernel: Kernel
        Default value:    from astropy.convolution import TrapezoidDisk2DKernel
    kernel = TrapezoidDisk2DKernel(radius=3, slope=1)
        Argument type:    string
        Acceptable values:
            - String value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    normalize: Normalize kernel
        Default value:    false
        Argument type:    boolean
        Acceptable values:
            - 1 for true/yes
            - 0 for false/no
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    interpolate: Interpolate no data pixel
        Default value:    true
        Argument type:    boolean
        Acceptable values:
            - 1 for true/yes
            - 0 for false/no
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputRaster: Output raster layer
        Argument type:    rasterDestination
        Acceptable values:
            - Path for new raster layer

    ----------------
    Outputs
    ----------------

    outputRaster: <outputRaster>
        Output raster layer

..
  ## AUTOGENERATED COMMAND USAGE END

