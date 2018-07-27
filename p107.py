import numpy as np


graph_text = [[int(num) for num in char_list] for char_list in [splitlist.split(',') for splitlist in [list.replace('-', '0') for list in open("D:\\graham_temp\\pEuler\\graph.txt").read().split('\n')]]]
graph = np.array(graph_text)
print graph
print sum(sum(array for array in graph))


def check_if_edge_is_removable(graph, edge_coordinates):
    if 


def pick_next_edge(current_graph):
    coordinates = sorted([(max(list), list.index(max(list)), current_graph.index(list)) for list in current_graph])[::-1]
    return [(coordinates[i], coordinates[i+1]) for i in range(0, len(coordinates), 2)]
print pick_next_edge(graph_text)
#


