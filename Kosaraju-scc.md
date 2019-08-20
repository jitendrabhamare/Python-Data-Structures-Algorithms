# Kosaraju's Two -Pass Algorithm

***
<ins>Theorem</ins></br>
Given a directed graph G, Kosaraju's Two-Pass Algorithm can computer Strongly Connected Components (SCC) in **O(m+n)** time.</br>
Where **m**: number of edges, **n**: number of nodes
***

<ins>Strognly Connected Components: Definition</ins></br>
The Strognly Connected Components (SCC) of a directed Grap G are the equivalence classes of the following relation: 

> u ~ v  <==> there exists a path from u to v and a path from v to u in G. 
