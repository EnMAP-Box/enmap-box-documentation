#!/bin/bash

# Define input and output directories
data_dir="somepath/data"
output_dir="somepath/output"

# Function to process a single file
process_file() {
    local f="$1"
    local output_dir="$2"

    # Generate output filename with the desired extension
    local output=$(basename "$f" | sed "s/\-METADATA.XML/.tif/")

    # Create a temporary directory
    local tmp_dir=$(mktemp -d)

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
}

# Export the function so that it can be used with parallel
export -f process_file

# Use GNU Parallel to process files in parallel (4 CPUs)
find "$data_dir" -name "*METADATA.XML" -print0 | parallel -j4 -0 process_file {} $output_dir
