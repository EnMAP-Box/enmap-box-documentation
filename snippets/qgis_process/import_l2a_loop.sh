#!/bin/bash

# Define input and output directories
data_dir="somepath/data"
output_dir="somepath/output"

# Iterate over files in the data directory
find "$data_dir" -name "*METADATA.XML" -print0 | while IFS= read -r -d '' f; do

    # Generate output filename with the desired extension
    output=$(basename "$f" | sed "s/\-METADATA.XML/.tif/")

    # Create a temporary directory
    tmp_dir=$(mktemp -d)

    # Run QGIS processing commands
    qgis_process run enmapbox:ImportEnmapL2AProduct \
        --file="$f" \
        --outputEnmapL2ARaster="$tmp_dir/temp.vrt"

    qgis_process run enmapbox:SaveRasterLayerAs \
        --raster="$tmp_dir/temp.vrt" \
        --creationProfile="GTiff INTERLEAVE=BAND COMPRESS=LZW PREDICTOR=2 BIGTIFF=YES" \
        --outputRaster="$output_dir/$output"

    # Clean up temporary directory
    rm -r "$tmp_dir"
done