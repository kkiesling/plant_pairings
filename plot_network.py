import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

# set size of map to display (75% to leave room for tool bar)
net = Network(height='100%', width='75%')

# load data into a datafram from csv file
df = pd.DataFrame()
df = df.from_csv('./plant-pairing-data.csv')
# honestly this info can probably be read from the csv?
col_str = "ANISE HYSSOP,BIG BLUESTEM GRASS,BLUE WILD INDIGO,BOTTLE GENTIAN,BUTTERFLY WEED,BUTTON BLAZING STAR,CARDINAL FLOWER,COLUMBINE,COMMON BLUE VIOLET,COMMON MILKWEED,CULVERS ROOT,GARDEN PHLOX,GREAT BLUE LOBELIA,HAIRY BEARDTONGUE,JACK-IN-THE-PULPIT,JACOB'S LADDER,JOE PYE WEED,LEAD PLANT,LITTLE BLUESTEM GRASS,MICHIGAN LILY,MIDLAND SHOOTING STAR,MONKEY FLOWER,OBEDIENT PLANT,ORANGE CONEFLOWER,PRAIRIE BLAZING STAR,PRAIRIE SMOKE,PURPLE CONEFLOWER,PURPLE PRAIRIE CLOVER,RED/ROSE MILKWEED,RIDDELL'S GOLDENROD,ROSE MALLOW,ROYAL CATCHFLY,SILKY ASTER,SKY BLUE ASTER,SMOOTH ASTER,SMOOTH/MARSH PHLOX,SOLOMON'S PLUME,SWAMP ROSE MALLOW,SWEET BLACK EYED SUSAN,SWEET JOE PYE-WEED,TALL THIMBLEWEED,TRILLIUM,TURTLEHEAD,VIRGINIA BLUEBELL,WILD BERGAMOT,WILD BLUE PHLOX,WILD GERANIUM,WILD LUPINE"
cols = col_str.split(',')
df.columns = cols

# intiate graph
graph = nx.Graph()
graph.add_nodes_from(cols)
soil_color = {'D': '#Be4025', 'M': '#149d1e', 'W': '#2525be'}

# first create each plant node
for planta in df.columns:
    # get node color based on soil moisture and careate node
    soil = df[planta]['soil moisture']
    color = soil_color[soil]
    graph.add_node(planta, color=color)

# then create edges (create all nodes first so we don't duplicate)
for planta in df.columns:
    for plantb in cols:
        # add edge where pairing exists
        if (df[planta][plantb] == 'x') and (planta != plantb):
            graph.add_edge(planta, plantb)

# convert to interactive graph
net.from_nx(graph)

# display
net.show_buttons()
net.show('plant_network.html')
