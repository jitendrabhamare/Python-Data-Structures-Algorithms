## Prim's minimum spanning tree algorithm
## Author: Jitendra Bhamare

"""
The input file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...

Aim is to run Prim's minimum spanning tree algorithm on this graph and report the overall cost of a 
minimum spanning tree (MST)--- an integer, which may or may not be negative --- in the box below.
"""

from queue import PriorityQueue
from math import inf
## Load input file
def load_graph_data(input_file):

    with open (input_file) as f:
        first_line = f.readline()
        first_line = first_line.split()
        num_nodes = int(first_line[0])
        num_edges = int(first_line[1])

        graph = {i: [] for i in range(1, num_nodes+1)}
        #print(graph)

        for line in f:
            line = line.split()
            src, dst, cost = int(line[0]), int(line[1]), int(line[2])
            graph[dst].append((src, cost))
            graph[src].append((dst, cost))

    #print(graph)
    return (graph, num_nodes, num_edges)

## Prim's MST Algorithm
def prim_algo(graph, start, num_nodes):

    keys = {start: 0}
    #print(keys)
    MSTcost = 0
    X = set()
    ## A priority queue ensures finds min-elements in O(log(n)) and deletion in O(1) time.
    frontier_queue = PriorityQueue()
    frontier_queue.put((keys[start], start))
    ## Main Loop
    while not frontier_queue.empty():

        current_node = frontier_queue.get()
        X.add(current_node[1])
        #print("current_node: {}".format(current_node[1]))
        #print("cummulative-cost: {}".format(MSTcost))

        ## Get all Frontiers of current Node
        for neighbor, key in graph[current_node[1]]:
            if neighbor not in X:
                if neighbor not in keys or key < keys[neighbor]:
                    keys[neighbor] = key
            
                    ## Add neighbor to the queue
                    #print("n: {}".format(neighbor))
                    frontier_queue.put((keys[neighbor], neighbor))    
        #print("keys: {}".format(keys))
    
    ## total cost of MST 
    for i in keys:
        MSTcost += keys[i]

    return MSTcost



if __name__ == '__main__':
    mygraph, num_nodes, num_edges = load_graph_data('edges.txt')
    #print(mygraph)
       
    cost = prim_algo(mygraph, 1, num_nodes)
    print(cost)
        

