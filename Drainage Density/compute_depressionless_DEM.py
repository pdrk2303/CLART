import numpy as np
import os
from pysheds.grid import Grid
from osgeo import gdal
import fiona

def compute_depressionless_dem(dem_path, output_dem, shape_file):
    with fiona.open(shape_file) as f:
        gj = [ft['geometry'] for ft in f]
    
    # Read DEM data using Pysheds
    grid = Grid.from_raster(dem_path)
    dem = grid.read_raster(dem_path, mask_geometry=gj)

    # Fill depressions in DEM
    pit_filled_dem = grid.fill_pits(dem, apply_mask=True)
    flooded_dem = grid.fill_depressions(pit_filled_dem, apply_mask=True)
    inflated_dem = grid.resolve_flats(flooded_dem, apply_mask=True)

    # save the depressionless_dem
    grid.to_raster(inflated_dem, output_dem, nodata=np.nan)



# Example usage:
shape_file = '/home/ictd/Desktop/Ankit/basins_india/mahi.shp'
output_folder = '/home/ictd/Desktop/Ankit/depressionless_dem'
srtm_directory = '/home/ictd/Desktop/Ankit/elevation'

tif = '.tif'
shp = '.shp'

for hgt_file in os.listdir(srtm_directory):
    if hgt_file.endswith(".hgt"):
        hgt_path = os.path.join(srtm_directory, hgt_file)
        tif_file = os.path.join(srtm_directory, os.path.splitext(hgt_file)[0] + ".tif")

        # Convert HGT to GeoTIFF using gdal_translate
        gdal.Translate(tif_file, hgt_path, format='GTiff')

        # Delete the original HGT file
        os.remove(hgt_path)

print("Conversion and deletion completed.")


tif_dir = srtm_directory
for filename in os.listdir(tif_dir):
    if os.path.isfile(os.path.join(tif_dir, filename)):
    	if filename.endswith('.tif'):
            # source = os.path.splitext(filename)[0]
            dem_file = os.path.join(tif_dir, filename)
            output_dem = os.path.join(output_folder, filename)
            print(f"Started: {output_dem}")
            compute_depressionless_dem(dem_file, output_dem, shape_file)
            print(f"Done: {output_dem}")
