# EnMAP-Box Documentation
This repository contains the EnMAP-Box Documentation

# Requirements
The packages in `requirements.txt` need to be installed.

Maintenance scripts in `/scripts` may require additional packages from PyQGIS and the EnMAP-Box source code.
They require that:
- a PyQGIS environment is available, i.e. you can run `import qgis`
- the EnMAP-Box source code repository (`enmap-box`) is installed into the same folder as this 
  documentation repository (`enmap-box-documentation`).


# Build the documentation

Open a terminal and run (linux) `make html`, or (windows) `make.bat html`.

