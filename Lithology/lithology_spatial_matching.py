

import geopandas as gpd

block_lith = gpd.read_file("C:/Users/n_sar/Downloads/lithology/mohanpur/Lithology.shp")
state_aquifer = gpd.read_file("C:/Users/n_sar/Downloads/yield_aquifer/PA_test_bihar.shp")

state_aquifer = state_aquifer.to_crs(block_lith.crs)

joined = gpd.sjoin(block_lith, state_aquifer, how="left", op="intersects")

joined.to_file("D:/priya iitd/Water Project/CLART/Lithology/final_spatial_matched_lithology/mohanpur/Lithology_final.shp")

print("Done")
