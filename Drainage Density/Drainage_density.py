import geopandas as gpd
import numpy as np

# Load watershed shapefile
watersheds = gpd.read_file("C:\Minor Project\Drainage density\watershed_boundaries\\angul_watershed.shp")  # Replace with your watershed shapefile path

# Load drainage lines shapefile
drainage_lines = gpd.read_file("C:\Minor Project\Drainage density\drainage_lines\\angul\dl_angul_new2.shp")

# Define influence factors for stream orders 1 to 7
influence_factors = [40/175, 35/175, 30/175, 25/175, 20/175, 15/175, 10/175]

# changing CRS for length calculation
drainage_lines = drainage_lines.to_crs(crs=3857)
watersheds = watersheds.to_crs(crs=3857)

watersheds['DD'] = None
watersheds['DD_stream'] = None
watersheds['str_len_km'] = None

# Iterate over each watershed
for index, watershed in watersheds.iterrows():
    # Filter drainage lines within the current watershed
    clipped_drainage_lines = gpd.clip(drainage_lines, watershed.geometry)

    stream_length = {}
    stream_drainage_density = {}
    
    # Calculate the total area of the current watershed
    area = watershed['area_sqkm']
    
    # Iterate over stream orders and calculate drainage density
    for stream_order, influence_factor in zip(range(1, 8), influence_factors):
        # Filter drainage lines for the current stream order
        stream_order_lines = clipped_drainage_lines[clipped_drainage_lines['ORDER'] == stream_order]
        
        # Calculate the sum of lengths for the current stream order
        total_length_stream_order = stream_order_lines.geometry.length.sum() / 1000  # Convert to kilometers
        
        # Calculate drainage density for the current stream order
        drainage_density = total_length_stream_order * influence_factor * 100 / area

        stream_length[stream_order] = total_length_stream_order
        stream_drainage_density[stream_order] = drainage_density
        
    # Create new columns in the 'watersheds' GeoDataFrame
    watersheds.at[index, 'DD'] = sum(stream_drainage_density.values()) 
    watersheds.at[index, 'DD_stream'] = stream_drainage_density
    watersheds.at[index, 'str_len_km'] = stream_length

# Restoring the original CRS
drainage_lines = drainage_lines.to_crs(crs=4326)
watersheds = watersheds.to_crs(crs=4326)


watersheds['DD'] = watersheds['DD'].astype(float)
watersheds['DD_stream'] = watersheds['DD_stream'].astype(object)
watersheds['str_len_km'] = watersheds['str_len_km'].astype(object)

# Save the results to a new shapefile
watersheds.to_file("C:\Minor Project\Drainage density\watershed_drainage_density\\angul_dd2.shp")
print("Shapefile exported")
