.. _documentation_style_guide:

=====
Documentation Guidelines
=====

The EnMAP-Box documentation is written in the reStructuredText(reST) format, coupled with some external libraries, e.g. Sphinx.
To keep things consistent, the following chapter contains guidelines on how to style the EnMAP-Box documentation.

Writing Guidelines
====================

Using the reST format for the documentation, allows to create several webpages with chapters, sections and subsections. To see the general style guidelines, follow the
`QGIS documentation guidelines <https://docs.qgis.org/3.22/en/docs/documentation_guidelines/index.html>`_.

The section *For Authors* guides you through the most important general rules for contributing to documentation, including the design of headings, inline tags and the insertion of captions and references.

The *Documentation* section in the `Pythons Developer's Guide <https://devguide.python.org/documentation/start-documenting/index.html>`_ summarises how to use Python to write documentation.
It describes the first steps in writing documentation and also gives some examples of how to include source code or hyperlinks.

In addition to the two guidelines mentioned above, we have developed some simple rules for EnMap Box documentation, which are described below.

1. reStructuredText
-----------------------

Basic inline markup
~~~~~~~~~~~~~~~~~~~

* *text* (italics) to emphasize something
* **text** (bold) to emphasize something strongly
* ``text`` (2 backquotes) for code samples, variables, filenames, etc.

In addition, when describing a workflow of some algorithm or tool, use the following instructions.

.. csv-table::
   :header: "Element", "Style", "Markup", "Example"
   :widths: 30, 10, 20, 40

   "Labels describing an interaction", GUI label, `:guilabel:`text` `, "Drag and drop the file from your file manager into the :guilabel:`Data Sources` panel."
   "Describing an algorithm in general", bold, `**text**`, "The EnMAP-Box offers **Spectral Library Windows** for visualizing spectra."
   "Captions of images, screenshots, etc.", italic, `*text*`, *Fig. 2: Example of adding a screenshot with explanation.*
   "Including files, samples, variables", file label + backquotes, `:file: ``text`` `, "Vector = :file:`agb_sonoma.gpkg`"

Numbering
~~~~~~~~~

If you want to describe a specific workflow or tutorial for the user, use numbering for the individual steps.
This way it is easier for the user to distinguish between information and actual steps and to follow along easily.

.. figure:: /img/numbering_workflow.png
   :width: 100%

*Workflow example with numbering*


2. Figures & Screenshots
------------------------

Screenshots with explanations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Font: Verdana
* Size: 14 pt
* Text color: RGB – 61-61-61
* Line color: RGB – 192-0-0
* Line width: 1 pt
* Description to the left of the screenshot at the level of the function to be explained
* Description text in box right-aligned

.. figure:: /img/screenshots_with_description.png
   :width: 100%

*Example of adding a screenshot with explanation.*

Positioning of info boxes and images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Info boxes, tooltips and notes should be aligned with the preceding text, i.e., if the info box follows a bulleted list, the box should also be indented.

.. figure:: /img/infoboxes.png
   :width: 100%

*Example of placing info boxes within / after bullet points.*

Images should always be centred, but can vary in size (adjust according to readability).
Also add a caption to the image if it is not placed between two bullet points.

.. figure:: /img/images_caption_example.png
   :width: 100%

*Placement of images for (a) within bullet points, (b) after body text*