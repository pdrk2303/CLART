
import rasterio
from rasterio.features import rasterize
from rasterio.transform import from_origin
import fiona

# Path to your vector shapefile
vector_file = "D:/priya iitd/Water Project/CLART/Lithology/final_spatial_matched_lithology/mandalgarh/Lithology_final.shp"

# Define the resolution (30m x 30m)
resolution = 0.000278 # in meters

# Define the column name to be used for rasterization
attribute_column = "Lithology_"

# Read the vector shapefile
with fiona.open(vector_file, "r") as shapefile:
    shapes = [(feature["geometry"], feature["properties"][attribute_column]) for feature in shapefile]
    bounds = shapefile.bounds
    print(f"Shapefile bounds: {bounds}")
    if bounds is None:
        # Calculate bounds manually
        all_geometries = [feature["geometry"] for feature in shapefile]
        bounds = fiona.collection.bounds(all_geometries)
        print(f"Calculated bounds: {bounds}")
# Define the raster metadata
minx, miny, maxx, maxy = bounds
width = int((maxx - minx) / resolution)
height = int((maxy - miny) / resolution)
transform = from_origin(minx, maxy, resolution, resolution)
# Rasterize the vector shapes based on the attribute column
raster = rasterize(
    shapes,
    out_shape=(height, width),
    fill=0,  # Background value
    transform=transform,
    all_touched=True,
    dtype=rasterio.float32  # or another appropriate data type
)

# Save the raster to a file
output_raster_file = "D:/priya iitd/Water Project/CLART/Lithology/final_spatial_matched_lithology/mandalgarh/Lithology_raster.tif"
with rasterio.open(
    output_raster_file, 'w',
    driver='GTiff',
    height=raster.shape[0],
    width=raster.shape[1],
    count=1,
    dtype=raster.dtype,
    crs=shapefile.crs,
    transform=transform,
) as dst:
    dst.write(raster, 1)

print(f"Rasterized shapefile saved as {output_raster_file}")

