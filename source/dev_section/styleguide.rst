.. _documentation_style_guide:

========================
Documentation Guidelines
========================

This documentation guideline provides an overview of the general style guidelines and on how to contribute to the documentation. It is based on the
`QGIS documentation guidelines <https://docs.qgis.org/3.22/en/docs/documentation_guidelines/index.html>`_.

The EnMAP-Box documentation is written in the reStructuredText(reST) format, coupled with some external libraries, e.g. Sphinx.
To keep things consistent, the following chapter contains guidelines on how to style the EnMAP-Box documentation.

Writing Guidelines
====================

Using the reST format for the documentation, allows to create several webpages with chapters, sections and subsections.
The section **For Writers** in the `QGIS documentation guidelines <https://docs.qgis.org/3.22/en/docs/documentation_guidelines/index.html>`_ guides you through the most important general rules for contributing to documentation, including the design of headings, inline tags and the insertion of captions and references.

Furthermore, you might want to take a look at the `Sphinx Python Documentation Generator Guide <https://devguide.python.org/documentation/start-documenting/index.html>`_  that
describes the first steps using Sphinx and reStructuredText in more detail and also gives some examples of how to include e.g. images, source code or hyperlinks.

In addition to the two guidelines mentioned above, we have developed some simple rules for EnMap Box documentation, which are described below.


1. reStructuredText
-----------------------

Basic inline markup
~~~~~~~~~~~~~~~~~~~

Use

* one asterisk for *italic text* (``*italic text*``) to emphasize something
* two asterisk for **bold text** (``**bold text**``) to emphasize something strongly
* two backquotes for ``code examples`` (````code examples````), variables, filenames, etc.

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

Use numbering to describe individual steps. This makes it is easier to distinguish
between information and actual steps and to follow them easily:

.. code-block::

 1. Enable the *Editing mode* by activating |mActionToggleEditing|.
 2. Now you can use the |mActionNewAttribute| button to add a new field (mind the type!)
 ...


.. figure:: /img/numbering_workflow.png
   :align: center

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
       :align: center
       :width: 800

*Example of adding a screenshot with explanation*

Positioning of info boxes and images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Info boxes, tooltips and notes should be aligned with the preceding text, i.e., if the info box follows a bulleted list, the box should also be indented.

    .. figure:: /img/infoboxes.png
       :align: center
       :width: 800

*Example of placing info boxes within / after bullet points*

Images should always be centred, but can vary in size (adjust according to readability).
Also add a caption to the image if it is **not** placed between two bullet points.

    .. figure:: /img/images_caption_example.png
       :align: center

*Placement of images for (left) after body text, (right) within bullet points*











.. Substitutions definitions - AVOID EDITING PAST THIS LINE
   This will be automatically updated by the find_set_subst.py script.
   If you need to create a new substitution manually,
   please add it also to the substitutions.txt file in the
   source folder.

.. |mActionNewAttribute| image:: /img/icons/mActionNewAttribute.svg
   :width: 28px
.. |mActionToggleEditing| image:: /img/icons/mActionToggleEditing.svg
   :width: 28px
