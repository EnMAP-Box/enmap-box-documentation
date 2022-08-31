#!/bin/bash

cd ..
set -e
if grep -qEi "(MINGW64_NT|Microsoft|WSL)" /proc/version &> /dev/null ; then
    echo "Run Sphinx on Windows 10 Bash"
    ./make.bat html
else
    echo "Run Sphinx on Linux"
    make html
fi