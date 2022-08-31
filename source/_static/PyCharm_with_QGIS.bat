:: set QGIS / OSGeo4W installation folder
set OSGEO4W_ROOT="C:\OSGeo4W64"

:: PyCharm executable
set PYCHARM="C:\Program Files\JetBrains\PyCharm 2018.2.4\bin\pycharm64.exe"

:: set defaults, clean path, load OSGeo4W modules (incrementally)
call %OSGEO4W_ROOT%\bin\o4w_env.bat
call qt5_env.bat
call py3_env.bat

:: lines taken from python-qgis.bat
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis
set PATH=%QGIS_PREFIX_PATH%\bin;%PATH%

:: make PyQGIS packages available to Python
set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis\python;%PYTHONPATH%

:: GDAL Configuration (https://trac.osgeo.org/gdal/wiki/ConfigOptions)
:: Set VSI cache to be used as buffer, see #6448 and
set GDAL_FILENAME_IS_UTF8=YES
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins

start "Start PyCharm aware of QGIS" /B %PYCHARM% %*

::@echo on
::@if [%1]==[] (echo run o-help for a list of available commands & cmd.exe /k) else (cmd /c "%*")
