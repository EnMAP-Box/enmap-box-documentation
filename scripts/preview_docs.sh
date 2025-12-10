#!/bin/bash

SOURCEDIR="source"
BUILDDIR="build"
SPHINXOPTS="$@"

sphinx-autobuild "$SOURCEDIR" "$BUILDDIR" $SPHINXOPTS