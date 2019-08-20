# Kosaraju's Two -Pass Algorithm

***
<ins>Theorem</ins></br>
Given a directed graph G, Kosaraju's Two-Pass Algorithm can computer Strongly Connected Components (SCC) in **O(m+n)** time.</br>
Where **m**: number of edges, **n**: number of nodes

***
<ins>Strognly Connected Components: Definition</ins></br>
The Strognly Connected Components (SCC) of a directed Grap G are the equivalence classes of the following relation: 

> u ~ v  <==> there exists a path from u to v and a path from v to u in G. 

***
<ins>Algorithm Design</ins></br>
- **Key** is to find right place to call Depth First Algorithm on Graph.i.e to find "leader" node in each SCC.</br>
- In orders to find leader-node, finishing time of a reverse-graph is computed. </br>
- Following are algorithm steps: </br>
    1. Let G-rev is G with all arcs reversed.
    2. Run DFS-loop on G-rev to compute "finishing time" of each node.
    3. Rus DFS-loop on G to discover SCC one-by-one. 
    
***
<ins>Solution></ins><br>


  
  
