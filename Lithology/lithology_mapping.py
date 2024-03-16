
import pandas as pd
import geopandas as gpd
import re

#table = pd.read_csv("D:/priya iitd/Water Project/CLART/GEC1997_RIF.csv")
table = gpd.read_file("C:/Users/n_sar/Downloads/yield_aquifer/PA_test_odisha.shp")
shapefile = gpd.read_file("C:/Users/n_sar/Downloads/lithology/mws_boundaries/angul/Lithology.shp")


def split(s):
    pattern = r'[ ,\/\\()&*-]'
    words = re.split(pattern, s)
    words = [word for word in words if word]
    return words


def word_wise_matching(s1, s2):
    score = 0
    s1 = s1.lower()
    s2 = s2.lower()
    s2 = split(s2)
    for i in s2:
        if i in s1:
            score += 1
            
    return score

print('Started')
count = 0
total = 0
for index_shapefile, row_shapefile in shapefile.iterrows():
    total += 1
    max_major_acquifer = None
    max_principle_acquifer = None
    max_score = 0
    
    for index_table, row_table in table.iterrows():
        score_1 = word_wise_matching(str(row_table['Principal_']), str(row_shapefile['GROUP_NAME']))

        score_2 = word_wise_matching(str(row_table['Major_Aqui']), str(row_shapefile['LITHOLOGIC']))
        
        score_3 = word_wise_matching(str(row_table['Principal_']), str(row_shapefile['LITHOLOGIC']))

        score_4 = word_wise_matching(str(row_table['Major_Aqui']), str(row_shapefile['GROUP_NAME']))
        
        score_5 = word_wise_matching(str(row_table['Age']), str(row_shapefile['AGE']))
        
        if score_5 > 0 and score_1 == 0 and score_2 == 0 and score_3 == 0 and score_4 == 0:
            continue
        
        total_score = score_1 + score_2 + score_3 + score_4 + score_5
        
        if total_score > max_score:
            max_score = total_score
            age = row_table['Age']
            max_major_acquifer = row_table['Major_Aqui']
            max_principle_acquifer = row_table['Principal_']
            acquifer_code = row_table['Major_Aq_1']
            rif = row_table['Recommende']
    
    if max_score != 0:
        count += 1
        shapefile.at[index_shapefile, 'Age'] = age
        shapefile.at[index_shapefile, 'Major_Aquifer'] = max_major_acquifer
        shapefile.at[index_shapefile, 'Principal_Aquifer'] = max_principle_acquifer
        shapefile.at[index_shapefile, 'Major_Aquifer_Code'] = acquifer_code
        shapefile.at[index_shapefile, 'Recommended_RIF'] = rif
        lithology_class = None
        if rif < 10:
            lithology_class = 3
        elif rif >= 10 and rif <= 15:
            lithology_class = 2
        elif rif > 15:
            lithology_class = 1
            
        shapefile.at[index_shapefile, 'Lithology_Class'] = lithology_class
    else:
        shapefile.at[index_shapefile, 'Age'] = None
        shapefile.at[index_shapefile, 'Major_Aquifer'] = None
        shapefile.at[index_shapefile, 'Principal_Aquifer'] = None
        shapefile.at[index_shapefile, 'Major_Aquifer_Code'] = None
        shapefile.at[index_shapefile, 'Recommended_RIF'] = None
        shapefile.at[index_shapefile, 'Lithology_Class'] = None
    
print('Number of rows classified: ', count)
print('Total number of rows: ', total)
print('Number of rows unclassified: ', total-count)
print('Loop Completed')   
shapefile.to_file("C:/Users/n_sar/Downloads/lithology/mws_boundaries/angul/Lithology_mapped.shp")
print('Done')  




