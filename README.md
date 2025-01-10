# EnMAP-Box Documentation
This repository contains the EnMAP-Box Documentation hosted in https://enmap-box.readthedocs.io



# Requirements
The packages in `requirements.txt` need to be installed:

`pip install --upgrade --user -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box-documentation/main/requirements.txt`

Maintenance scripts in `/scripts` may require additional packages from PyQGIS and the EnMAP-Box source code.
They may require that:
- a PyQGIS environment is available, i.e. you can run `import qgis`
- the EnMAP-Box source code repository (`enmap-box`) is either 
    
  a) installed into the same folder
    ````
    <repositories>/enmap-box
                  /enmap-box-documentation
    ```` 
  or 
  
  b) specified by the environmental variable `ENMAPBOX_REPO=<repositories>/enmap-box`

# Branching

The `main` branch contains corresponds to the `develop` branch of the EnMAP-Box source code (
will be changed to `main` after the EnMAP-Box source code to github.)

Release branches, e.g. `release_3.10` contain the documentation related to the corresponding EnMAP-Box versions 
as they are released in the QGIS plugin repository.


# Files and Folders 

| Folder   | Content                                                 |
|----------|---------------------------------------------------------|
| source   | Documentation files (*.rst)                             |
| scripts  | Maintenance scripts, e.g. to generate *.rst files       |
| snippets | Python snippets, e.g. to create widgets for screenshots |

# How to contribute?


Everyone can contribute to this documentation using git [pull-requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests).
If you never have used git before, we recommend to read a basic git tutorial first, e.g. https://rogerdudler.github.io/git-guide/ or https://github.com/git-guides.

1. [Create a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) 
   of this repository (hereafter referred as `enmap-box-documentation-fork`).
2. [Clone & checkout](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) 
   your fork on your local computer:

   * https: ``git clone https://github.com/mygithubaccount/enmap-box-documentation-fork.git``
   * ensure that the packages in ``requirements.txt`` are installed to your python environment, e.g. running
     ``python -m pip install -r requirements.txt``

3. Change the EnMAP-Box documentation. 
   * E.g. add a new tutorial `*.rst` files to `/source/usr_section/application_tutorials`
   * It is recommended to use a proper IDE like PyCharm or text editor for your modifications

4. Inspect your changes in a browser:
   * run (linux) `make html`, or (windows) `make.bat html` to create the webpage's html files to ``build/html``
   * start a local server that hosts the html files: 
     Windows: ``python -m http.server build\html ``
     Linux: ``python -m http.server build/html ``
   * open the webpage in your local browser using the URL http://localhost:8000/ 

5. Commit your changes with message that describe what you have done, e.g. `added tutorial XY` or `corrected typos`.
6. [Push](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository) your changes to your 
   remote repository ``https://github.com/mygithubaccount/enmap-box-documentation-fork.git``
7. Repeat the previous steps if you need to add further modifications
8. When done, publish your modifications in the official EnMAP-Box documentation creating a 
   [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

# Build the documentation

* open a bash shell and run `./scripts/create_docs.sh` (windows/linux bash shell), or 
* run (linux) `make html`, or (windows) `make.bat html`, or
* run `sphinx-autobuild `

# Substitutes

Substitute allow you to "recycle" code definitions

1. Define a substitute in `source/substitutions_manual.txt`. E.g. write ``.. |my_icon| image:: img/icons/myicon.png``
2. Use ``|my_icon|`  in any *.rst file you like.
3. Run ``python scripts/create_substitutes.py`` to append the ``|my_icon|`` to any *.rst file where it is used
4. Run ``make.bat html`` to build the documentation.


