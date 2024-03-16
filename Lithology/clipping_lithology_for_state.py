

import geopandas as gpd

# Read the aquifer map shapefile
aquifer_map = gpd.read_file("C:/Users/n_sar/Downloads/yield_aquifer/PA_test_yield_with_rif.shp")

# Filter features based on the state value
aquifer_map_br = aquifer_map[(aquifer_map['state'] == 'RJ')]

# Save the filtered aquifer map to a new shapefile
aquifer_map_br.to_file("C:/Users/n_sar/Downloads/yield_aquifer/PA_test_rajasthan.shp")
