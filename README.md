# CLART
### Abstract
The aim of the project is to use GIS based methods for the site suitability analysis of feasibility of NRM works in India. Groundwater recharge potential is used as a metric to divide the area under study into various classes. The type of NRM for a location is based on said classification.
### Introduction
The Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA), promises unskilled manual work to every adult for at least 100 days in rural parts of the country. Huge funds (Rs. 73,000 crore in the last budget) are allocated for this, making it the government's one of the top rural focused schemes. Roughly 60-70% of these resources are spent on Natural Resource Management (NRM) works like check dams, percolation tanks, and irrigation channels. The overall focus of the scheme is on ensuring higher incomes for farmers by increasing the water availability and productivity of land. The traditional way of suitable site identiﬁcation for these structures has been based on local people’s opinion, and taking into consideration factors such as geomorphology, climate, annual rainfall, vegetation cover, distances from farms and so on.

However, misidentification of suitable locations for NRM works has resulted in non-operation, non-utilization and inefficient investment. On a state or national level, Geographic Information System (GIS) based methods for site suitability analysis are much more time saving and cost effective than field studies. Recommended sites can be cross verified by field workers resulting in a smoother workflow.
### Research Methodology
Weighted multi-criteria overlay analysis is a methodology useful for identifying the relationship between multiple feature layers. This is done by superimposing multiple layers of datasets that represent different themes/criteria. 

Depending on how the different layers impact the classification under consideration (groundwater recharge potential in this case), these layers can be assigned different weights to result in a composite map combining different attributes and dataset geometries. 

For GWRP, the following input layers are considered - lithology, drainage density and lineaments. This recharge potentiality in weighted combination with slope percentage results in a feasibility score layer which can be used to determine the type of NRM work most suitable for the area in consideration.

The analysis was initially done on QGIS Desktop manually for the district of Jamui, Bihar, and then automated using Python. The automation allowed easy extension of the process for the whole of India. The most recent work involves transferring the preprocessed layers to Google Earth Engine to create a reconfigurable assessment tool with dynamic scoring to allow flexibility based on requirement.
