@echo off
setlocal

:: Get the directory where the batch script is located
set "SCRIPT_DIR=%~dp0"

:: Remove trailing backslash from SCRIPT_DIR for consistency
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

:: Define directories
set "SOURCEDIR=%SCRIPT_DIR%\..\source"
set "BUILDDIR=%SCRIPT_DIR%\..\build"

:: Run sphinx-autobuild with all passed arguments (%*)
sphinx-autobuild "%SOURCEDIR%" "%BUILDDIR%" %*

endlocal
