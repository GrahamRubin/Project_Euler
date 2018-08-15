import numpy as np
from itertools import permutations
import copy
np.set_printoptions(threshold=np.inf)
graph_text = [[int(num) for num in char_list] for char_list in [splitlist.split(',') for splitlist in [list.replace('-', '0') for list in open("D:\\graham_temp\\pEuler\\graph.txt").read().split('\n')]]]
# graph = np.array(graph_text)
# print graph
# print sum(sum(array for array in graph))
small_graph = [[0, 16, 12, 21, 0, 0, 0], [16, 0, 0, 17, 20, 0, 0],
                        [12, 0, 0, 28, 0, 31, 0], [21, 17, 28, 0, 18, 19, 23],
                        [0, 20, 0, 18, 0, 0, 11], [0, 0, 31, 19, 0, 0, 27],
                        [0, 0, 0, 23, 11, 27, 0]]


def check_edge(graph, indices):
    bool = False
    for i in graph[indices[0]]:
        count = 0
        if i != 0 and graph[indices[0]].index(i) != indices[0] and graph[indices[0]].index(i) != indices[1]:
            for j in graph[graph[indices[0]].index(i)]:
                if j != 0: # and graph[graph[indices[0]].index(i)].index(j) != indices[0]:
                    count += 1
        if count > 1:
            bool = True
            break
    for i in graph[indices[1]]:
        count = 0
        if i != 0 and graph[indices[1]].index(i) != indices[1] and graph[indices[1]].index(i) != indices[0]:
            for j in graph[graph[indices[1]].index(i)]:
                if j != 0: #and graph[graph[indices[1]].index(i)].index(j) != indices[1]:
                    count += 1
        if count > 1 and bool:
            return True
    return False


def czech_edge(graph, indices):
    # try edge tracing method. if this edge were removed, can you still access every other edge
    temp_graph = graph
    temp_graph[indices[0]][indices[1]] = 0
    temp_graph[indices[1]][indices[0]] = 0
    x_list = list(range(len(graph))).remove(indices[0])
    y_list = list(range(len(graph))).remove(indices[1])



def try_remove(graph, edge_coordinates):
    if check_edge(graph, (edge_coordinates[1], edge_coordinates[2])):
        graph[edge_coordinates[1]][edge_coordinates[2]] = 000
        graph[edge_coordinates[2]][edge_coordinates[1]] = 000


def pick_next_edge(current_graph):
    coordinates = []
    [[coordinates.append((value, list.index(value), current_graph.index(list))) for value in list if value != 0] for list in current_graph]
    coordinates = sorted(coordinates)[::-1]
    coordinates = [coordinates[i] for i in range(0, len(coordinates), 2)]
    # print len(coordinates)
    old_sum = sum(sum(array) for array in current_graph)//2
    print old_sum*2
    count = 0
    maximum = 0
    maxgraph = copy.deepcopy(current_graph)
    while count < 513:
        temp_graph = copy.deepcopy(current_graph)
        temp_coordinates = copy.deepcopy(coordinates)
        pointer = -1 * count
        length = len(coordinates)
        while pointer != length:
            try_remove(temp_graph, temp_coordinates[pointer])
            pointer += 1
        new_sum = old_sum - (sum(sum(val) for val in temp_graph)//2)
        if new_sum > maximum:
            maximum = new_sum
            maxgraph = copy.deepcopy(temp_graph)
        # print new_sum
        count += 1
        # print (current_graph)
    for line in maxgraph:
        for element in line:
            str(element)
            if len(element) == 1:
                element = element + '  '
            elif len(element) == 2:
                element = element + ' '
        print line
    return maximum

print pick_next_edge(graph_text)*2



