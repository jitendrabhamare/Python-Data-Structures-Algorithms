## Kosaraju's Algorithm to find strongly connected components (SCC)
## Author: Jitendra Bhamare

import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

def main():
    ###  Load an input text file and generate graph and reversed graph from it. 
    input_file = open("SCC.txt", "r")
    data = input_file.readlines()
    # Declare num of nodes from input files. always define with one extra node
    num_nodes = 875715  

    graph = [[] for i in range(num_nodes)]
    rgraph = [[] for i in range(num_nodes)]

    for item in data:
        item = item.split()
        graph[int(item[0])] += [int(item[1])]
        rgraph[int(item[1])] += [int(item[0])]

    ### Intialize lists for pass1
    explored = [False] * num_nodes
    leader = [0] * num_nodes
    #order = [0] * num_nodes
    order = []

    ## DFS_Loop function
    def DFS_Loop(graph, pass_list):
        global t # Num of nodes processed so far
        t = 0
        global s # Current source vertex
        s = None

        for i in pass_list:
            if explored[i] == False:
                s = i # assign to start node
                DFS(graph, i)

    ## Recursive DFS Function
    def DFS(graph, i):
        explored[i] = True

        for neighbor in graph[i]:
            if explored[neighbor] == False:
                DFS(graph, neighbor)
        global t
        t += 1
        # order list is used in second pass 
        order.append(i) # append and reverse list works much faster than prepend
        global s
        leader[s] += 1

    ## Run DFS_Loop on rev graph
    pass1_list = range(num_nodes-1, 0, -1)
    DFS_Loop(rgraph, pass1_list)

    ## Intialize lists for pass2
    order.reverse()
    pass2_list = order
    #print(pass2_list)
    new_size = len(order)+1 # Will not consider disconnected graphs
    order = [0] * new_size 
    explored = [False] * new_size
    leader = [0] * new_size

    ## Run DFS_Loop on graph
    DFS_Loop(graph, pass2_list)

    #print("finishing order: {}".format(order))
    #print("leader : {}".format(leader))
    #print("explored : {}".format(explored))

    #getting 5 biggest scc
    leader.sort(reverse=True)
    print("First largest 5 SCCs: {}".format(leader[:5]))


thread = threading.Thread(target=main)
thread.start()    
