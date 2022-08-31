# EnMAP-Box Documentation
This repository contains the EnMAP-Box Documentation

# Requirements
The packages in `requirements.txt` need to be installed.

Maintenance scripts in `/scripts` may require additional packages from PyQGIS and the EnMAP-Box source code.
They require that:
- a PyQGIS environment is available, i.e. you can run `import qgis`
- the EnMAP-Box source code repository (`enmap-box`) is installed into the same folder as this 
  documentation repository (`enmap-box-documentation`).

# Branching

The `main` branch contains corresponds to the `develop` branch of the EnMAP-Box source code. 

Release branches, e.g. `release_3.10` contain the documentation related to the corresponding EnMAP-Box versions 
as they are released in the QGIS plugin repository.


# Files and Folders 

| Folder   | Content                                                 |
|----------|---------------------------------------------------------|
| source   | Documentation files (*.rst)                             |
| scripts  | Maintenance scripts, e.g. to generate *.rst files       |
| snippets | Python snippets, e.g. to create widgets for screenshots |


# Build the documentation

Open a terminal and run (linux) `make html`, or (windows) `make.bat html`.

