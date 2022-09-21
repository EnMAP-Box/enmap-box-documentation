# EnMAP-Box Documentation
This repository contains the EnMAP-Box Documentation hosted in https://enmap-box.readthedocs.io



# Requirements
The packages in `requirements.txt` need to be installed.

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


# Build the documentation

* open a bash shell and run `./scripts/create_docs.sh` (windows/linux bash shell), or 
* run (linux) `make html`, or (windows) `make.bat html`.


