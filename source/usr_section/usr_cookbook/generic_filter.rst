Generic Filter (Majority)
=========================

With the Spatial Generic Filter Processing Algorithm you can use the `scipy generic_filter <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.generic_filter.html>`_
function to write your own spatial filter functions.

In this example we will write a mode filter (also known as majority filter). This kind of filter is often used to
smooth classification results (reduce salt-and-pepper effects in the image). It calculates the mode of all values in a specifiable
neighborhood around a pixel (e.g. 3x3 pixel window) and assigns this value to the pixel.

#. In the Processing Toolbox go to and open :menuselection:`Convolution, Morphology and Filtering --> Spatial Generic Filter`
#. Select an input raster under :guilabel:`Raster`
#. In the :guilabel:`Code` text window you can enter python code. Delete the existing content and enter the following

   .. code-block:: python

      from scipy.ndimage.filters import generic_filter
      import numpy as np
      from scipy.stats import mode

      def filter_function(invalues):
         invalues_mode = mode(invalues, axis=None, nan_policy='omit')
         return invalues_mode[0]

      function = lambda array: generic_filter(array, function=filter_function, size=3)


#. Specify the output raster location and click :guilabel:`Run`

.. figure:: /img/modefilter.png
   :width: 100%

   Majority filter applied to classification image: original classification (left), majority filtered 3x3 window (middle), majority filtered 5x5 window (right)

.. tip::

   Also have a look at the `scipy.stats.mode <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mode.html>`_ documentation. You can change
   the window size by altering the ``size`` parameter in the :keyword:`generic_filter` function.

   You could further improve the function above by putting constraints on the definition of majority (for example, only update the original value if
   the frequency of the modal value is higher than 50 percent)