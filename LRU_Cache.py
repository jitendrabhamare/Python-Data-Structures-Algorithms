# DNode object that has key and value as attributes
class DNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        s = "{}".format(self.key, self.value)
        return s

class DLList:
    """ 
        Double LinkedList is used. That can append and remove any node
        with O(1) time complexity.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, node):
        # Add a node and set it as head
        if self.head is None:
            self.head = node
            self.tail = self.head

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        
        self.size += 1
        return node

    def remove(self, node):
        # if head == tail == node
        if node.prev is None and node.next is None:
            #print("yo, node is isolated")
            self.head = None
            self.tail = None

        # if node is head
        elif self.head == node:
            #print("yo, node is head")
            self.head = node.next
            self.head.prev = None
            node.next = None
            
        # if node is tail
        elif self.tail == node:
            #print("yo, node is tail")
            self.tail = node.prev
            self.tail.next = None
            node.prev = None

        # if node is somewhere in the middle
        else:
            #print("yo, node is in the middle")
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None

        self.size -= 1

        return node

    def __repr__(self):
        s = "<LRU> \n___________________\n"
        node = self.head
        while node:
            s += str(node.key)
            s += "\n___________________\n"
            node = node.next
        s += "<MRU>"
        return s


# LRU_Cache comprised of both DLL and dict data structure. 
# Both Dict and DLL operations ensure -  time complexity to be O(1)         
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.lru_buff = DLList()
        self.cache = dict()

    def get(self, key=None):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key is None:
            raise ValueError("Please provide a key as an argument!")

        # Cache Miss
        if self.cache.get(key) is None:
            return -1

        # Cache Hit
        else:
            # remove item from lru_buff and add it back at tail (MRU)
            temp = self.lru_buff.remove(self.cache[key])
            self.lru_buff.append(temp)
            return temp.value

    def set(self, key=None, value=None):
            
        if key is None :
            raise ValueError("Please provide a key as an argument!")
        # If key already presrnt in cache
        if key in self.cache:
            # Update lru_buff order
            temp = self.lru_buff.remove(self.cache[key])
            self.lru_buff.append(temp)
      
        # If key is not present in cache
        else:
            # Check if cache is full, remove LRU entry (head)
            if self.lru_buff.size == self.capacity:
                lru_node = self.lru_buff.head    
                del_node = self.lru_buff.remove(lru_node)
                del self.cache[del_node.key]

            # Create and add a node to lru_buff and
            # Add it to the cache-dict as {key: node}
            node = self.lru_buff.append(DNode(key, value))
            self.cache[key] = node
        
    def __repr__(self):
        s = "\nLRU cache: \n"
        s += "capacity: {}".format(self.capacity)
        s += "\n"
        s += "keys:   "
        s += " | ".join([str(key) for key in self.cache.keys()])
        s += "\n"
        s += "values: "
        s += " | ".join([str(value.value) for value in self.cache.values()])
        s += "\n"
        return s


### Test Case 1 : Given Test-case       
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print(our_cache)
print(our_cache.lru_buff)    


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache)
print(our_cache.lru_buff)   

# test-case 2 : set with Pass no value
our_cache.set(10)   # Should store value as None
print(our_cache)
print(our_cache.lru_buff)   

# test-case 3: set pass no value, no key
our_cache.set()   # Should raise an exception

## test-case 4: get with no key
our_cache.get()   #Should raise an exception

    
