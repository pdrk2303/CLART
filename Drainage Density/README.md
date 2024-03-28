## Drainage Density
Drainage network of the watershed helps in visualizing which areas have a high groundwater recharge. Drainage density is directly related to slope and inversely proportional to permeability. The steeper the slope with low permeability, the higher the drainage density, thus less infiltration and more surface runoff.
#### Source:
SRTM Digital Elevation Model (DEM) data at a resolution of about 1:60k (30m by 30m) is used to find for each pixel the number of its neighbors which drain into it. The D8 algorithm is used for flow directions and thresholding is done to get drainage lines for India.
#### Pre-Processing:
Drainage density is a measurement of the sum of the channel lengths per unit area. The drainage lines are processed to measure the sum of line lengths per unit area using the QGIS Line Density tool, which calculates for each pixel the line density as the sum of lengths of the vectors in the surrounding unit area weighted by their thickness and returns a raster mask with each pixel having the value of the corresponding line density. This  drainage density mask is now georeferenced to the respective state for ease of visualization.

![Picture2](https://github.com/pdrk2303/CLART/assets/116311921/ebec2f3f-fe48-464c-90c6-f47ef34836a5)

**Note**: Low drainage density is more likely to dominate in highly permeable, dense vegetation, and low relief areas. To quantify drainage density, the range of values observed in the basin where the area is situated is evenly divided into three classes. The first class is assigned a score of 1, the second class is assigned a score of 2, and the third class is assigned a score of 3.
The drainage lines are reprojected to 7755 coordinate reference system (crs) before computing drainage density.
 #### Scoring: 
 Low drainage density is more likely to dominate in highly permeable, dense vegetation, and low relief areas. To quantify drainage density, the range of values observed in the basin where the area is situated is evenly divided into three classes. The first class is assigned a score of 1, the second class is assigned a score of 2, and the third class is assigned a score of 3.

 
 Take a look at this for detailed steps: [link](https://docs.google.com/document/d/19gBgpVYu7dTAb7CEB2PdCqDUCEBYj1ZM29jngxH_6Hk/edit?usp=sharing)
