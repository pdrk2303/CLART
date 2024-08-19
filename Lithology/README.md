## Lithology
Lithology is a representation of the underlying rock structure of the area under consideration. Infiltration is the process of seepage of water into the groundwater table. Lithologic structure of a place determines the infiltration factor of the area and hence is an important feature in the assessment.

#### Source: 
The state-wise lithology data has been downloaded as shapefiles manually from Bhukosh.

For detailed steps to download, take a look at this: [link](https://docs.google.com/document/d/19nxvW8ZIbofpXj_ZIMOvLDRcjStKedZLECCiPhS42RU/edit?usp=drive_link)
#### Pre-Processing: 
The downloaded shapefiles are analyzed to understand the different lithology types in the area. These distinct lithology types are then correlated with the 60 principal aquifer types, along with their corresponding rainfall infiltration factors sourced from the Rainfall Infiltration Factor table outlined in the GEC 1997 report. These types can be combined into broader classes depending on the requirement of the study. Individual classes are extracted and rasterized at a resolution of 1:60k (30m by 30m). These rasters can be combined to generate a state lithology mask which is georeferenced to the respective state for ease of visualization.
#### Scoring: 
The rainfall infiltration factor (rif) from the GEC 1977 report is used as a measure of recharge potential. Lithology types are categorized into three classes based on their respective rainfall infiltration factors: those with values greater than 15 are assigned a score of 1, those falling between 10 and 15 receive a score of 2, and lithology types with rif values below 10 are assigned a score of 3.

GEC 1997 Report: [link](http://www.angelfire.com/nh/cpkumar/publication/Lgwa.pdf) (Page no. 9,10,11)
#### Steps to Generate the Lithology Raster:
1. Download the lithology shape files for the desired block from Bhukosh. (Link provided in the [Source](#source) section)
2. The state wise aquifer maps are already available in the [yeild_aquifer](./yield_aquifer) folder.
3. Run the [lithology_spatial_matching.py](./lithology_spatial_matching.py) script with block_lith as the lithology shapefile of the block and state_aquifer as the aquifer shapefile of the block's corresponding state. This will add the Lithology Class as an attribute to the various lithology groups present in the block.
4. Now to get the Lithology Raster with Lithology Class as the pixel value run the (rasterizing_vectors.py)(./rasterizing_vectors.py) script to rasterize the vector file generated in the previous step.
