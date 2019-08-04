# Huffman Coding ############################

### Problem

### Design Logic
- Created a node class- 'HuffmanNode' that has following properties. - char, frequency, left child and right child. 
- Created a class- 'HuffmanCoding' that include methods including huffman_encoding, huffman_decoding and all required helper methods. 
- steps for encoding and decoding
    step 1: The 'build_freq_table()' method takes a string and determine the relevant frequencies of the characters store them in a dictionary, also create a HuffmanNode object of each item. 
 Time complexity: O(n). Where n is number of character in an input string in worst case scenario, no char is repeated.
 Space complexity: Function of 2 * n. Hence O(n)

    step 2: Created a helper 'sort_node_list()' method. 
            - It converts Huffman node objects into tuples (char, freq, left, right) - [TC: O(n), SC: O(n)]
            - sorts them in rev order according to freq values- [TC: O(nlogn), SC: O(n)]
            - Convert back them into Huffman Nodes so that sorted Huffman node list returned. [TC: O(n), SC: O(n)]
            Overall for step 2, time complexity : O(nlogn) and Space complexity is O(n)

    step 3: 'build_huffman_tree()' method. 
            - If node is None, return None. (Corner case)
            - If input text is just one char or repeatation of one char. create a dummy node. (corner case) 
            - Sort a node list (using step 2) and pop two nodes with lowest frequencies. Create a parent node 
              (i.e. make the two nodes as a children of this node) with new value of freq as summantion of freqs of children.  
            - push back parent node into sorted list. 
            - repeat untill there is only one node remaining is a node-list
            - TC for this step would be a fuction of number of node and step 2. [i.e. O(nlogn * n].
            - SC is depends on depth of a tree. worstcase scenario depth is n. hence SC is O(n * n)


    step 4: - The 'encode()' and recursive 'encode_helper()' methods are used to encode each char according to HuffmanTree structure 
              and store them into a dictionary. 
              TC: O(d) where d is depth of a tree and depth is n for worstcase, hence TC: O(n), 
              SC - size of dict which is const * n. hence SC: O(n)
            - 'generate_bitsteam()' creates encoded bit stream using corresponding dictionary keys. 
              TC- O(n), SC - const * n = O(n)
    step 5: 'huffman_encoding()' method use all the helper function. 
            TC: Overall Time complexity from step 1-4 is O(n^2.logn)
            SC: For step 1-4 is O(n^2)
    step 6: 'huffman_decioding()' uses reverse dictionary values to decode bitstream into a text value.
            TC: O(n)
            Sc: O(n)

    Thus Overall Time complexity: O(n^2.logn) and space complexity is O(n^2)

    Note: Using inbuild priority queue data structure time complexity can be improved (as sorting could have been avoided.)
          However, I preferred using all data-structures using scratch and decided to use list and sort approach. 

