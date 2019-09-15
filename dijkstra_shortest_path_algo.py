from ast import literal_eval
from queue import PriorityQueue

### Load input file and create graph data-structure
def load_graph_data(input_file):
    path_graph = {}
    with open(input_file) as file:
        for line in file:
            line_content = line.split()
            path_graph[int(line_content[0])] = [literal_eval(edge) for edge in line_content[1:]]
    return path_graph

## Dijkstra's Shortest Path Algorithm using Heap(Priority Queue)
def dijkstra_shortest_path(graph, start, goal):

    ## A priority queue ensures finds min-elements in O(log(n)) and deletion in O(1) time.
    frontier_queue = PriorityQueue()

    ## Computed shortest Path distance
    dijk_score = {start: 0}

    ## Initialize a queue with start with it's dijk_score
    print(dijk_score)
    frontier_queue.put((dijk_score[start], start))

    ## Main Loop
    while not frontier_queue.empty():

        ## get a node from queue with it's min dijk_score
        #print("front-queue: {}".format(frontier_queue.queue))
        current_node = frontier_queue.get()
        #print("min-node: {}".format(current_node))

        if current_node[1] == goal:
            return dijk_score

        ## Get all frontiers of the current node
        for neighbor, length in graph[current_node[1]]:
            dijk_score_tentative = dijk_score[current_node[1]] + length

            # Proceed only if neighbor is not explored or its explored then 
            # it's tentative-score value should be less than dijk_score[neighbor]
            if neighbor not in dijk_score or dijk_score_tentative < dijk_score[neighbor]:
                dijk_score[neighbor] = dijk_score_tentative

                ## Add neighbor to frontier Queue
                frontier_queue.put((dijk_score[neighbor], neighbor))

    return dijk_score




if __name__ == '__main__':
    mygraph = load_graph_data('dijkstraData.txt')
    print(mygraph)

    short_dist_set = dijkstra_shortest_path(mygraph, 1, 201)
    print(short_dist_set[7])
    print(short_dist_set[37])
    print(short_dist_set[59)
    print(short_dist_set[82])
    print(short_dist_set[99])
    print(short_dist_set[115])
    print(short_dist_set[133])
    print(short_dist_set[165])
    print(short_dist_set[188])
    print(short_dist_set[197])

