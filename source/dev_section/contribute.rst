.. _contribute:

Contribute
##########

The EnMAP-Box is a freely available, platform-independent software designed to process hyperspectral remote sensing data,
and particularly developed to handle data from the EnMAP sensor.

The EnMAP-Box source code is hosted in a public git repository at https://github.com/EnMAP-Box/enmap-box.

Approved `QGIS plugin <https://www.qgis.org/en/site>`_ versions (“production releases”) are available in the QGIS Plugin Repository https://plugins.qgis.org/plugins/enmapboxplugin/.


The development of the EnMAP-Box is funded within the EnMAP scientific preparation program under the
DLR Space Administration (mission lead) and GFZ Potsdam (scientific lead) with resources from the
German Federal Ministry for Economic Affairs and Energy.


Everyone is welcome to contribute to the EnMAP-Box

Submit a bug report or feature request
======================================

In case you experience issues with the EnMAP-Box, do not hesitate to submit a
ticket to our `Issue Tracker <https://github.com/EnMAP-Box/enmap-box/issues>`_. You are also welcome
to post feature requests or pull requests.

It is recommended to check that your issue complies with the
following rules before submitting:

*  Verify that your issue is not being currently addressed by other
   `issues <https://github.com/EnMAP-Box/enmap-box/issues??q=is%3Aissue+is%3Aopen>`_
   or `pull requests <https://github.com/EnMAP-Box/enmap-box/pulls/>`_.

*  If you are submitting a bug report, please:

    * Report a short description how to reproduce it

    * If an exception is raised, please provide the full traceback.

    * If necessary, provide a link to the data that causes the bug

    * If not feasible to include a reproducible snippet, please be specific about
      what part of the EnMAP-Box (functions, widget) are involved and the shape of the data

    * Include your operating system type and version number of QGIS, Qt and the EnMAP-Box.

    * Please ensure that code snippets and error messages are formatted in appropriate code blocks.

    .. note::
        You can use this `Markdown syntax <https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax>`_
        to style your issues.





Provide source code
===================

If your are not an EnMAP-Box core developer, the preferred way to contribute your code code is to use
`pull requests <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`__.


1. :ref:`Fork the EnMAP-Box repository<contribute_fork>`
2. :ref:`Clone your fork<contribute_clone>`
3. :ref:`Modify the source code <contribute_modify>`
4. :ref:`Commit your modifications <contribute_commit>`
5. :ref:`Push your modification to your fork <contribute_push>` and
6. :ref:`Create a pull request <contribute_pull_request>`

.. _contribute_fork:

1. Create a fork on GitHub
--------------------------

Forking the EnMAP-box repository allows you to modify the EnMAP-Box code as you like and backup your contributions in a
separated GitHub repository. To create a fork,

1. log in to GitHub and visit https://github.com/EnMAP-Box/enmap-box

2. Click '+' and `Fork this repository`

3. Select a name and workspace for your EnMAP-Box fork, hereafter called *enmap-box-fork*

..  .. raw:: html

..    <div><video width="90%" controls muted><source src="../_static/videos/forking.1.create.fork.mp4"
..                type="video/mp4">Your browser does not support HTML5 video.</video>
     <p><i>Create an EnMAP-Box fork in GitHub</i></p></div>


Please read https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks
for details how you can create your own fork of the EnMAP-Box repository.


.. _contribute_clone:

2. Clone the forked EnMAP-Box repository
----------------------------------------

Follow `these steps <https://github.com/EnMAP-Box/enmap-box#how-to-clone>`_ but replace the EnMAP-Box repository url
with that of your fork. Clone *enmap-box-fork* to your local disk::

    git clone --recurse-submodules git@github.com/myusername/enmap-box-fork.git


Go into the repository folder and force to checkout the *develop* branch.

    cd enmap-box-fork

Add the EnMAP-Box repository as *upstream* repository::

    git remote add upstream https://github.com/EnMAP-Box/enmap-box


.. note::

    From now on, you can synchronize your fork with the EnMAP-Box repository by::

        $git fetch upstream main
        $git merge upstream/main

    to get the latest updates from the *main* branch. Call::

        $git push

    to upload them to the remote github.com/myusername/enmap-box-fork.git

Now install python requirements and run the initial setup for the EnMAP-Box repository, as described in :ref:`dev_installation`





.. _contribute_modify:

3. Modify the local repository
------------------------------

As you like, you can continue modifying the EnMAP-Box code in the *develop* branch or create a new one 'my_modifications'::

    $ git checkout -b my_modifications


.. _contribute_commit:

4. Commit your changes
----------------------

Save your changes by committing them to your local repository::

    $ git add modified_files
    $ git commit -a -m 'added x, modified y and fixed z' -s

Please use signed commits to label your individual contribution visible.
Even better, use GnuPG-signed commits (-S).

.. _contribute_push:

5. Push changes back to your fork
---------------------------------

A push will upload your changes to github.com/myusername/enmap-box-fork.git::

    $ git push

.. _contribute_pull_request:

6. Create a pull request
------------------------


Open the GitHub webpage of your fork and create a pull request.
The pull request will inform us on the changed you made.

Before you create a pull request, please check the following:

* make sure that every source code file provides a :ref:`licence notice <contribute_apply_licence_terms>`

* make sure your code passes the tests and provide tests if your like to provide new functionality, like EnMAP-Box Applications

* make sure your code is commented and documented

* make sure your name is listed in the :code:`CONTRIBUTORS.md`

* update your feature branch to the current EnMAP-Box *develop* branch::

        git fetch upstream develop
        git merge upstream/develop


* rebase your changes and push them to your forked repository::

        git push -f


* describe your pull request with a helpful title, e.g using the following labels:

    * :code:`[feature] <title>` a new feature
    * :code:`[fix] <title>` a fix for a known issue. If possible, please refer to existing issue numbers like in `#123 #124`.


Documentation
=============

The EnMAP-Box documentation is based on `Sphinx-build reStructured text <https://www.sphinx-doc.org/en/master/>`_
and hosted at https://enmap-box.readthedocs.io/en/latest .

The documentation source code, i.e. *.rst* files, are hosted in the :code:`/source` folder in
https://github.com/EnMAP-Box/enmap-box-documentation

Please read https://github.com/EnMAP-Box/enmap-box-documentation#readme for how you can
contribute to the EnMAP-Box documentation repository and the :ref:`Style Guide <documentation_style_guide>` for a more detailed overview of the general styling.

.. _contribute_licensing:

Licensing
=========

The software produced for the EnMAP-Box is licensed according to the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License (SPDX short identifier: GPL-3.0), or (if desired) any later version.
See either https://www.gnu.org/licenses/gpl-3.0.en.html or https://opensource.org/licenses/GPL-3.0 for further details of the license.

A copy of this license is part of the EnMAP-Box repository (`LICENSE.txt <https://github.com/EnMAP-Box/enmap-box/blob/main/LICENSE.md>`_) and delivered with each release of an EnMAP-Box plugin.

The EnMAP-Box documentation is published under the terms of the Creative Commons 1.0 Universal (CC0) License.
See https://creativecommons.org/publicdomain/zero/1.0/legalcode for further details of the license.


.. _contribute_apply_licence_terms:

Applying License Terms
----------------------
Each source code contribution to the central repository should include a reference to the GPL-3 license terms at the beginning of the file::

    """
    ***************************************************************************
        <file name> - <short description>
        -----------------------------------------------------------------------
        begin                : <month and year of creation>
        copyright            : (C) <year> <creator>
        email                : <main address>

    ***************************************************************************
        This program is free software; you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation; either version 3 of the License, or
        (at your option) any later version.
                                                                                                                                                     *
        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this software. If not, see <https://www.gnu.org/licenses/>.
    ***************************************************************************
    """

An example from the source code can be found here: `enmapbox/__init__.py <https://github.com/EnMAP-Box/enmap-box/blob/main/enmapbox/__init__.py>`_

Images and other multimedia content from the EnMAP-Box documentation, i.e files within the EnMAP-Box repositories :code:`doc/source` folder,
are published under the terms of the `CC0 license <https://creativecommons.org/publicdomain/zero/1.0/legalcode>`_.



.. _contribute_CLA:

Contributor License Agreements (CLA)
------------------------------------

The purpose of CLAs are to clearly define the terms under which intellectual property has been contributed to the
EnMap-Box and thereby allow us to defend the project should there be a legal dispute regarding the software at some
future time.

.. _contribute_ICLA:

Individual Contributor License Agreement (ICLA)
...............................................

The EnMap-Box Consortium desires that all maintainers and contributors of ideas, code, or documentation to the
EnMAP-Box project complete, sign, and submit an ICLA.

A signed ICLA is required to be on file before an individual is given commit rights to the EnMap-Box repository.
The ICLA form for filling and signing is available `here <../_static/docs/20200820_individual-contributor-license-agreement_GPL3.0_EnMAP_v.1.0.pdf>`__.

The ICLA is not tied to any employer, so it is recommended to use one's personal information, e.g. for email address in
the contact details, rather than an email address provided by an employer.


.. _contribute_CCLA:

Corporate Contributor License Agreement (CCLA)
..............................................

For a corporation that has assigned employees to work on the EnMap-Box, a CCLA is available for contributing
intellectual property via the corporation, that may have been assigned as part of an employment agreement.

Note that a CCLA does not remove the need for every developer to sign their own ICLA as an individual, which
covers both contributions which are owned and those that are not owned by the corporation signing the CCLA.

The CCLA legally binds the corporation, so it must be signed by a person with authority to enter into legal
contracts on behalf of the corporation. The CCLA form for filling and signing is available
`here <../_static/docs/20200820_corporate-contributor-license-agreement_GPL3.0_contributoragreements_v.1.0.pdf>`_.


.. _contribute_submit_CLAs:

Submitting License Agreements
.............................

Documents may be submitted by email and signed by hand or by electronic signature.
The files should be named icla.pdf and icla.pdf.asc for individual agreements;
ccla.pdf and ccla.pdf.asc for corporate agreements. Zip files, other archives, or links to files are not accepted.
The files must be attached to the mail.

When submitting by email, please fill the form with a pdf viewer, then print, sign, scan all pages into a single
pdf file, and attach the pdf file to an email to enmapbox@enmap.org. If possible, send the attachment from the email address
in the document. Please send only one document per email.

If you prefer to sign electronically, please fill the form, save it locally (e.g. icla.pdf), and sign the file by
preparing a detached PGP signature. For example, gpg --armor --detach-sign icla.pdf

The above will create a file icla.pdf.asc. Send both the file (icla.pdf) and signature (icla.pdf.asc) as attachments
in the same email. Please send only one document (file plus signature) per email. Please do not submit your public key. Instead, please upload your public key to pgpkeys.mit.edu.


.. _contribute_DCO:

Developer Certificate of Origin (DCO)
.....................................

Contributors who have not signed an ICLA are in a somewhat fuzzy spot. If they make a large contribution,
or many contributions, then the EnMap-Box maintainers will likely ask to submit an ICLA. However, for small fixes,
infrequent and other minimal or sporadic contributions the terms for licensing and intellectual property still must
be clarified.

For this purpose, barriers for contributing are minimized and contributors pinky swear that they're
submitting their own work or rather certify that they adhere to the requirements of the DCO defined in
version 1.1 or later at https://developercertificate.org/ by signing-off their pull requests or similar ways of
contributing.

The DCO is very Git-centric, and it only relies on commit metadata.

Indeed, signing-off a commit is just about appending a Signed-off-by. For example a commit like::

    $ git commit -m 'Fixes issue XYZ' -s

will create a commit message as in::

    commit b2c150d3aa82f6583b9aadfecc5f8fa1c74aca09
    Fixes issue XYZ
    Signed-off-by: Erwin Gerwin <erwin.gerwin@streetcat.com>


Even this approach introduces a low barrier for contributions, it is very easy to use whatever email address you want
for a commit, and the sign-off is just text. Since the issue of trust is important the use of GnuPG signatures
in Git commits is recommended additionally, e.g. with::

    $ git commit -s -S (makes GnuPG-signed commits, and)
    $ git log --show-signature (shows GnuPG signatures in the log history)
    $ git merge --verify-signatures branch (ensures that all commits are signed and valid before performing a merge)

Having to use GnuPG for all commits can be a bit daunting.


.. _contribute_test_and_ci:

Tests and Continuous Integration
================================

Please provide some tests that show if your source code works right.
Unit tests should be located in the repositories :code:`enmapboxtesting` folder.

To run all tests call::

    $ set CI=True
    $ python -m nose2 -s enmapboxtesting



.. note::
    The environmental variable *CI=True* is used to inform test routines to **not enter** the GUI thread.
    If unset, some widgets might pop-up and wait for your input to terminate.

To run the unit tests in *test_mytests.py*, call::

    $ python -m nose2 -s enmapboxtesting test_mytests

