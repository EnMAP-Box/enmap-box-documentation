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


# Preview the documentation locally

## Classic
Open a bash shell and run `./scripts/preview_docs.sh`. 
If run successfully, the documentation will be available at http://localhost:8000/

`preview_docs.sh` is a wrapper for [sphinx-autobuild](https://github.com/sphinx-doc/sphinx-autobuild#readme****)
````bash
cd <repo dir>/enmap-box-documentation
`sphinx-autobuild source build`
````

## Docker

### Documentation preview

1. Run `docker compose up docs` in the root directory of the repository.
2. Open a browser and go to http://localhost:8000/

### QGIS + EnMAP-Box runtime image

The Dockerfile also contains a `qgis-enmapbox` target. This image installs QGIS from the QGIS LTR
Ubuntu packages, installs the Linux Python dependencies without conda, creates a QGIS user profile
named `EnMAP-Box`, and installs the latest `EnMAP-Box 3` plugin from the QGIS plugin repository into
that profile.

Build the image:

````bash
docker build --target qgis-enmapbox -t enmapbox-qgis .
````

Run a non-GUI smoke test:

````bash
docker run --rm enmapbox-qgis qgis-plugin-manager check --version 3.44
````

Run QGIS on a Linux/X11 desktop:

````bash
xhost +local:docker
docker compose --profile qgis up qgis
````

The QGIS profile is created inside the container at
`/home/enmapbox/.local/share/QGIS/QGIS3/profiles/EnMAP-Box`.

### Interactive testing inside the container

If you want to explore the plugin from Python, import the EnMAP-Box package itself, not
`enmapboxplugin.plugin`.

Headless smoke test:

````bash
docker run --rm qgis-enmapbox:latest python3 -u - <<'PY'
from enmapbox.testing import start_app
from enmapbox import initAll

app = start_app()
initAll()
print("EnMAP-Box initialized successfully")
PY
````

Interactive shell:

````bash
docker run -it --rm qgis-enmapbox:latest python3
````

Then run:

````python
from enmapbox.testing import start_app
from enmapbox import initAll, EnMAPBox

app = start_app()
initAll()

enmapbox = EnMAPBox(None)
print(enmapbox)
````

If you want to work with the plugin path directly, add the installed plugin root directory to `sys.path`
and import `enmapbox`, not `plugin`:

````python
import sys
sys.path.insert(0, '/home/enmapbox/.local/share/QGIS/QGIS3/profiles/EnMAP-Box/python/plugins/enmapboxplugin')
from enmapbox.gui.enmapboxgui import EnMAPBox
````


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
