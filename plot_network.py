import argparse
# import wget
import pandas as pd
import matplotlib.pyplot as plt

import networkx as nx
from pyvis.network import Network

from lxml import html


# from slimit import ast
# from slimit.parser import Parser
# from slimit.visitors import nodevisitor

import urllib

def args_parse():
    """collect user inputs from command line"""

    formatter = argparse.RawDescriptionHelpFormatter

    description = """ """

    usage = ""

    examples = """ """

    parser = argparse.ArgumentParser(description=description,
                                     usage=usage,
                                     epilog=examples,
                                     formatter_class=formatter)
    parser.add_argument('plantfile',
                        action='store',
                        nargs=1,
                        type=str,
                        help='path to a text file with plant scientific names ' +
                        'to include in pairings map. One plant name per line. ' +
                        'If -c is set, names should be common names.'
                        )
    parser.add_argument('-a', '--all',
                        action='storetrue',
                        required=False,
                        dest='all',
                        help='if set, all plants within one degree ' +
                        'of separation from the provided list will be mapped.',
                        )
    parser.add_argument('-c', '--common',
                        action='storetrue',
                        required=False,
                        dest='common',
                        help='if set, all plants within one degree ' +
                        'of separation from the provided list will be mapped.',
                        )


    args = parser.parse_args()
    return args


def parse_plants(fname):
    """parse plants list"""

    f = open(fname, 'r')
    all_lines = f.readlines()
    plant_list = []
    for line in all_lines:
        plant_list.append(line)

    return plant_list


def collect_data(plant_list, all_plants, common):
    """scrape webiste for data from Prairie Moon Nursery"""

    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
              'AppleWebKit/537.11 (KHTML, like Gecko) '
              'Chrome/23.0.1271.64 Safari/537.11',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
              'Accept-Encoding': 'none',
              'Accept-Language': 'en-US,en;q=0.8',
              'Connection': 'keep-alive'}

    # scrape website

    url_base = 'https://www.prairiemoon.com/seeds/'

    if common:
        name_type = 'common-name'
    else:
        name_type = 'latin-name'

    all_plants = []

    for i in range(2, 29):

        if i == 1:
            url = url_base
        else:
            url = url_base + '?page={}'.format(i)

        # get webpage

        req = urllib.request.Request(url=url, headers=header)
        page = urllib.request.urlopen(req).read().decode("utf-8")
        htmltree = html.fromstring(page)
        all_spans = htmltree.cssselect('span')
        for span in all_spans:
            # all_plants.append(span.find('result.name'))
            span_str = html.tostring(span).decode("utf-8")
            if name_type in span_str:
                plant_name = span_str.split('>')[-2].split('<')[0]
                all_plants.append(plant_name)


    print(all_plants)


def main():

    # collect user inputs
    # args = args_parse()

    # plant_list = parse_plants(args.plantfile[0])

    collect_data([], True, True)

    # colled data

if __name__ == '__main__':
    main()


# net = Network(height='100%', width='75%')
#
# df = pd.DataFrame()
# df = df.from_csv('./plant-pairing-data.csv')
# col_str = "ANISE HYSSOP,BIG BLUESTEM GRASS,BLUE WILD INDIGO,BOTTLE GENTIAN,BUTTERFLY WEED,BUTTON BLAZING STAR,CARDINAL FLOWER,COLUMBINE,COMMON BLUE VIOLET,COMMON MILKWEED,CULVERS ROOT,GARDEN PHLOX,GREAT BLUE LOBELIA,HAIRY BEARDTONGUE,JACK-IN-THE-PULPIT,JACOB'S LADDER,JOE PYE WEED,LEAD PLANT,LITTLE BLUESTEM GRASS,MICHIGAN LILY,MIDLAND SHOOTING STAR,MONKEY FLOWER,OBEDIENT PLANT,ORANGE CONEFLOWER,PRAIRIE BLAZING STAR,PRAIRIE SMOKE,PURPLE CONEFLOWER,PURPLE PRAIRIE CLOVER,RED/ROSE MILKWEED,RIDDELL'S GOLDENROD,ROSE MALLOW,ROYAL CATCHFLY,SILKY ASTER,SKY BLUE ASTER,SMOOTH ASTER,SMOOTH/MARSH PHLOX,SOLOMON'S PLUME,SWAMP ROSE MALLOW,SWEET BLACK EYED SUSAN,SWEET JOE PYE-WEED,TALL THIMBLEWEED,TRILLIUM,TURTLEHEAD,VIRGINIA BLUEBELL,WILD BERGAMOT,WILD BLUE PHLOX,WILD GERANIUM,WILD LUPINE"
# cols = col_str.split(',')
# df.columns = cols
#
# graph = nx.Graph()
# graph.add_nodes_from(cols)
# soil_color = {'D': '#Be4025', 'M': '#149d1e', 'W': '#2525be'}
#
# for planta in df.columns:
#     soil = df[planta]['soil moisture']
#     color = soil_color[soil]
#     graph.add_node(planta, color=color)
#     for plantb in cols:
#         if (df[planta][plantb] == 'x') and (planta != plantb):
#             graph.add_edge(planta, plantb)
#
# net.from_nx(graph)
#
# net.show_buttons()
# net.show('plant_network.html')
#
