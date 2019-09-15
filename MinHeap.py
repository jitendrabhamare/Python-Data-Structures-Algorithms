class MinHeap(object):

    def __init__(self):
        #self.capacity = capacity
        self.size = 0
        self.items = []

    def get_leftchild_index(self, parent_index):
        return 2 * parent_index + 1

    def get_rightchild_index(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        return (child_index -1) // 2

    def has_left_child(self, index):
        return self.get_leftchild_index(index) < self.size

    def has_right_child(self, index):
        return self.get_rightchild_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.items[self.get_leftchild_index(index)]

    def right_child(self, index):
        return self.items[self.get_rightchild_index(index)]

    def parent(self, index):
        return self.items[self.get_parent_index(index)]


    def swap(self, index1, index2):
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    def peek(self):
        if self.size == 0:
            return None
        else:
            return items[0]

    def pop(self):
        if self.size == 0:
            return None
        else:
            item = self.items[0]
            self.items[0] = self.items[self.size-1]
            self.size -= 1
            self.heapify_down()
            return item

    def push(self, item):
        self.items.append(item)
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size-1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_leftchild_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_rightchild_index(index)

            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index

    """ heapify_down method with recursion 
    def heapify_down(self, index):

        if self.has_left_child(index):
            # Find smallest node index among parent, left and right children
            if self.left_child(index) < self.items[item]:
                smallest_node_index = self.get_leftchild_index(index)
            else:
                smallest_node_index = index

            if self.has_right_child(index) and self.right_child(index) < self.items[smallest_node_index]:
                smallest_node_index = self.get_rightchild_index(index)

            # Recurse if parent is not smallest
            if smallest_node_index != index:
                swap(index, smallest_node_index)
                self.min_heapify(smallest_node_index)
            
    """               
    
    
    
#MinHeap testing 
if __name__ == "__main__":
    my_heap = MinHeap()
    my_list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    for n in my_list:
        my_heap.push(n)

    print("Min-Heap: {}".format(my_heap.items))
    my_heap.push(0)
    print("Final Min-Heap: {}".format(my_heap.items))
    my_heap.pop()
    my_heap.pop()
    my_heap.pop()
    print("Final Min-Heap: {}".format(my_heap.items))
    

