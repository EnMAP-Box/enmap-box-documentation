#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

SOURCEDIR="$SCRIPT_DIR/../source"
BUILDDIR="$SCRIPT_DIR/../build"
SPHINXOPTS="$@"

sphinx-autobuild "$SOURCEDIR" "$BUILDDIR" $SPHINXOPTS