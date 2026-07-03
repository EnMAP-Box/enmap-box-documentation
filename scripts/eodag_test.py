import os
from eodag import EODataAccessGateway

# Initialize EODAG and prioritize the DLR Geoservice
dag = EODataAccessGateway()
dag.set_preferred_provider("dlr_eoc_geoservice")

# Define your search parameters
search_criteria = {
    "collection": "ENMAP_HSI_L2A",
    "geom": {"lonmin": 13.0, "latmin": 52.0, "lonmax": 13.5, "latmax": 52.5}, # Example: Berlin area bounding box
    "start": "2023-05-01",
    "end": "2023-09-30"
}

print("Searching DLR Geoservice for EnMAP products...")
search_results = dag.search(**search_criteria)
print(f"Found {len(search_results)} products.")

# Define where to save the files
download_dir = os.path.join(os.getcwd(), "enmap_downloads")
os.makedirs(download_dir, exist_ok=True)

# Download and automatically extract the products
print("Downloading products...")
downloaded_paths = dag.download_all(
    search_results,
    outputs_prefix=download_dir,
    extract=True
)

print(f"Download complete. Files saved to: {download_dir}")