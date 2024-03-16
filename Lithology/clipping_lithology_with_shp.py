

import geopandas as gpd

# Read the two shapefiles
aquifer_shapefile = gpd.read_file("C:/Users/n_sar/Downloads/yield_aquifer/PA_test_yield.shp")
boundary_shapefile = gpd.read_file("C:/Users/n_sar/Downloads/administrative_boundary/mandalgarh_block_boundary.shp")

# Ensure both shapefiles have the same CRS
aquifer_shapefile = aquifer_shapefile.to_crs(boundary_shapefile.crs)

# Clip the aquifer shapefile with the boundary shapefile
clipped_aquifer = gpd.clip(aquifer_shapefile, boundary_shapefile)

# Save the clipped aquifer shapefile
clipped_aquifer.to_file("C:/Users/n_sar/Downloads/yield_aquifer/mandalgarh_PA_with_rif.shp")

print("DONE")
