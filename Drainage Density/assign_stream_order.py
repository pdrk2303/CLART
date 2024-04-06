import os
import fiona
from shapely.geometry import LineString, Point
import networkx as nx

dl_dir = '/home/ictd/Desktop/Ankit/dl'
so_dir = '/home/ictd/Desktop/Ankit/so_basins'

def add_coord_attributes(filename):
    # Load drainage lines shapefile
    # drainage_lines_shapefile = "/home/ictd/Desktop/Ankit/drainage_lines/mahi_dl_pysheds_updated.shp"
    drainage_lines_shapefile = os.path.join(dl_dir, filename)

    x = "temp.shp"

    # Define a function to find start and end nodes based on geometry
    def find_start_end_nodes(geometry):
        start_node = geometry['coordinates'][0]
        end_node = geometry['coordinates'][-1]
        return start_node, end_node

    # Open the input shapefile and create a new shapefile with additional attributes
    with fiona.open(drainage_lines_shapefile, 'r') as input_src:
        schema = input_src.schema.copy()
        schema['properties']['start_node'] = 'str'
        schema['properties']['end_node'] = 'str'

        with fiona.open(x, 'w', 'ESRI Shapefile', schema) as output_src:
            for input_feature in input_src:
                attributes = input_feature['properties']
                geometry = input_feature['geometry']

                start_node, end_node = find_start_end_nodes(geometry)

                #attributes['start_node'] = f"{start_node[0]}, {start_node[1]}"
                #attributes['end_node'] = f"{end_node[0]}, {end_node[1]}"

                """output_feature = {
                    'type': 'Feature',
                    'geometry': geometry,
                    'properties': attributes
                }"""

                input_feature['properties']['start_node'] = f"{start_node[0]}, {start_node[1]}"
                input_feature['properties']['end_node'] = f"{end_node[0]}, {end_node[1]}"

                output_src.write(input_feature)



def final_code(filename):


    drainage_lines_shapefile = "temp.shp"

    G = nx.Graph()

    #print(G.number_of_nodes())
    edges = []

    with fiona.open(drainage_lines_shapefile) as src:
        for feature in src:
            attributes = feature['properties']
            start_node = attributes['start_node']
            end_node = attributes['end_node']
            start_coordinates = tuple(map(float, attributes['start_node'].split(',')))
            end_coordinates = tuple(map(float, attributes['end_node'].split(',')))
            
            #if start_coordinates in node_attributes and end_coordinates in node_attributes:
            G.add_edge(start_coordinates, end_coordinates, stream_type=attributes['stream_typ'])
            edges.append((start_coordinates, end_coordinates))
            
    print(G.number_of_edges())
    print(G.number_of_nodes())

    #stream_orders = {(edge[0], edge[1]): 1 for edge in G.edges()}
    #x = G.has_edge((4576963.739944668, 4057026.964562115), (4576483.760990102, 4056786.9962220737))
    #print(x)
    for edge in G.edges():
        G.edges[edge]['stream_order'] = -1
        

    changed = True
    c = 0
    while True:
        for edge in edges:
            if G.edges[edge]['stream_type'] == "start" and G.edges[edge]['stream_order'] != 1:
                #print("yes")
                G.edges[edge]["stream_order"] = 1
            elif G.edges[edge]['stream_type'] == "intermediate":
                neighbors = list(G.neighbors(edge[0]))
                point = edge[0]
                if edge[1] in neighbors:
                    neighbors.remove(edge[1])
                

                        
                neighbors_so = [G.edges[(edge[0], neighbor)]['stream_order'] for neighbor in neighbors]
                
                if neighbors_so == []:
                    #print('cry')
                    continue
    
                f = False
                for i in neighbors_so:
                    if i == -1:
                        f = True
                        break
                
                if f:
                    continue
                
                
                max_order = max(neighbors_so)
                
                s = set(neighbors_so)
                if len(s) > 1 and G.edges[edge]['stream_order'] != max_order:
                    #print("no1")
                    G.edges[edge]['stream_order'] = max_order
                elif len(s) == 1 and G.edges[edge]['stream_order'] != max_order + 1:
                    #print("no2")
                    G.edges[edge]['stream_order'] = max_order + 1

        c += 1
        
        flag = False    
        for edge in G.edges():
            if G.edges[edge]['stream_order'] == -1:
                print("Not yet completed")
                flag = True
                break
        
        if not flag:
            print("Completed")
            break
        
    print(c)
    print("done")

    



    x = os.path.join(so_dir, filename)

    with fiona.open(drainage_lines_shapefile, 'r') as input_src:
        schema = input_src.schema.copy()
        schema['properties']['ORDER'] = 'int'

        with fiona.open(x, 'w', 'ESRI Shapefile', schema) as output_src:
            for input_feature in input_src:
                attributes = input_feature['properties']
                geometry = input_feature['geometry']
                
                start_node = tuple(map(float, attributes['start_node'].split(',')))
                end_node = tuple(map(float, attributes['end_node'].split(',')))
                
                edge = (start_node, end_node)
                
                so = G.edges[edge]['stream_order']
        
                input_feature['properties']['ORDER'] = so

                output_src.write(input_feature)
            




for filename in os.listdir(dl_dir):
    if os.path.isfile(os.path.join(dl_dir, filename)):
    	if filename.endswith('.shp'):
            add_coord_attributes(filename)
            final_code(filename)
            print("done")
            print(filename)
          

