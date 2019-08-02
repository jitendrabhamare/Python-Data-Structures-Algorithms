# Least Recently Used Cache 

### Logic Design
- To design LRU Cache two data structures are used, namely Doubly LinkedList (DLL) and Dictionary. 
- `Dictioanry` contains keys as cache-keys and values as cache `<node-object-reference>` (node has 4 attributes namely key, value, prev and next). Thus any node can be accessed in `O(1)` time. 
- `DLL` stores node of a cache which are linked in LRU order (with head as LRU and Tail as MRU). Whenever a cache entry
  is accessed (set/get), it removes corresponding node from DLL and append it in the end as Tail, Thus it maintains 
  order of `Least Recently Used` entries. Both remove and append operations take `O(1)` time complexity.
- Using Dictionary Data Structure, user can retrieve stored cache value (by key) with `O(1)` time complexity. 
- When cache is full, Head of DLL (LRU) is removed and corresponding entry in the Dictionary is deleted. 
- \__repr\__ method is overwritten to get custom print statement of a 'LRU Cache' object. 

### Efficiency

#### Time Complexity
- Overall time complexity: `O(1)` since all operations are constant.  

#### Space complexity
- If cache capcity is n (i.e. input size), each node has 4 attributes (4), it creates DLL with n nodes (4 * n) 
  and dict (1 + 4 * n) with n key-value pairs. Space increase linearly with respect to n. Therefore, spece complexity is constant * n i.e. `O(n)`.
  
### Code
[LRU Cache](https://github.com/jitendrabhamare/Python-Data-Structures-Algorithms/blob/master/LRU_Cache.py)
