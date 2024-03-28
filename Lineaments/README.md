## Lineaments
Lineaments are linear features in a landscape which represents cracks or faults in the surface of the earth. Since the depression allows water to get collected around the lineament, they form good regions for groundwater to be recharged.
#### Source: 
The state-wise lineaments data has been taken from Bhuvan at a resolution of 1:50k (25m by 25m) by sending out a WMS request and generating .tif files from the packets.
#### Pre-Processing:
The lineament layers are processed to generate a proximity mask. The Proximity (Raster Distance) algorithm computes the distance from the center of each pixel to the center of the nearest pixel on a target pixel (a lineament in this case). The  generated raster proximity map is now scanned for pixels with a distance of less than a buffer value (currently 2m) and selected pixels are exported to form a Lineaments Buffer Mask. This mask is now georeferenced to the respective state for ease of visualization.
#### Scoring:
Since the lineaments facilitate groundwater recharge, the areas/pixels within the said lineament buffer (2m) are assigned a score of 10, and remaining pixels are assigned a score of 1.
