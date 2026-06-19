.. _appli_tuto:

Application Tutorials
#####################

Use this catalog to choose an application-oriented EnMAP-Box workflow. The tutorials range from
introductory examples with prepared data to specialized applications for machine learning, geology,
ocean colour, soil mapping, vegetation analysis, atmospheric preprocessing, and HPC processing.

.. container:: tutorial-summary

   Select a tutorial by topic, method, or processing environment. Internal links open tutorials in this
   documentation; external links point to companion tutorials maintained by the corresponding application teams.

Tutorial Catalog
****************

.. rst-class:: sphinx-datatable tutorial-catalog

.. list-table::
   :widths: 6 30 42 22
   :header-rows: 1

   * - No.
     - Tutorial
     - Focus
     - Best for
   * - 1
     - :doc:`Regression-based unmixing of urban land cover <urban_unmixing/tutorial>`
     - Estimate urban land-cover fractions from hyperspectral imagery using spectral libraries and regression-based unmixing.
     - Urban mapping, mixed pixels
   * - 2
     - :doc:`Regression-based mapping of forest aboveground biomass <biomass_regression/tutorial>`
     - Build forest aboveground biomass maps from imaging spectroscopy data and reference observations.
     - Forest biomass modelling
   * - 3
     - :doc:`Ocean Colour analysis with ONNS <ocean_colour/onns>`
     - Use the OLCI Neural Network Swarm workflow to retrieve water quality parameters from ocean colour data.
     - Coastal and inland waters
   * - 4
     - :doc:`EnGeoMAP 3.2 Manual <engeomap/tutorial_engeomap>`
     - Classify geological surface materials from hyperspectral data with user-defined endmembers and colour schemes.
     - Mineral mapping
   * - 5
     - :doc:`EnSoMap tutorial <ensomap/tutorial_ensomap>`
     - Generate and validate topsoil property maps from hyperspectral imagery.
     - Soil property mapping
   * - 6
     - :doc:`Spectral Libraries: An Introduction <spectral_library/spectral_library_tut>`
     - Learn how to load, inspect, edit, and use spectral libraries in EnMAP-Box.
     - First spectral library workflows
   * - 7
     - :doc:`EnMAP-Box in HPC environments / SLURM <hpc/run_on_hpc>`
     - Install and run QGIS, EnMAP-Box processing algorithms, and SLURM jobs on a command-line HPC system.
     - Batch processing, HPC users
   * - 8
     - :doc:`SpecDeepMap semantic segmentation tutorial <specdeepmap/tutorial_specdeepmap>`
     - Train and apply deep-learning segmentation models for spectral imagery.
     - Spatial-spectral pixel classification
   * - 9
     - `Manual Retrieval of Vegetation Variables using IVVRM <https://enmap-box-lmu-vegetation-apps.readthedocs.io/en/latest/tutorials/IVVRM_tut.html>`__
     - Retrieve vegetation variables with the IVVRM application workflow.
     - Vegetation variables
   * - 10
     - `SIO and DASF for N Estimation <https://trier-for-enmap-box.readthedocs.io/tuts/tut1.html>`__
     - Estimate nitrogen using SIO and DASF workflows from companion EnMAP-Box tools.
     - Nitrogen estimation
   * - 11
     - `EnPT tutorial <https://enmap.git-pages.gfz-potsdam.de/GFZ_Tools_EnMAP_BOX/EnPT/doc/tutorial.html>`__
     - Run EnMAP Processing Tool workflows for EnMAP data preparation and preprocessing.
     - EnMAP preprocessing

.. toctree::
   :maxdepth: 1
   :numbered:
   :hidden:

   urban_unmixing/tutorial.rst
   biomass_regression/tutorial.rst
   ocean_colour/onns.rst
   engeomap/tutorial_engeomap.rst
   ensomap/tutorial_ensomap.rst
   Spectral Libraries <spectral_library/spectral_library_tut.rst>
   HPC environments / SLURM <hpc/run_on_hpc.rst>
   Spectral Imaging Deep Learning Mapper (SpecDeepMap): A Tutorial for Semantic Segmentation <specdeepmap/tutorial_specdeepmap.rst>
   9. Manual Retrieval of Vegetation Variables using IVVRM <https://enmap-box-lmu-vegetation-apps.readthedocs.io/en/latest/tutorials/IVVRM_tut.html>
   10. SIO and DASF for N Estimation <https://trier-for-enmap-box.readthedocs.io/tuts/tut1.html>
   11. EnPT <https://enmap.git-pages.gfz-potsdam.de/GFZ_Tools_EnMAP_BOX/EnPT/doc/tutorial.html>
