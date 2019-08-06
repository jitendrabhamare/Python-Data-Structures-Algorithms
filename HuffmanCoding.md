# Huffman Coding ############################

### Problem

> A **Huffman code** is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.
> 
> The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.
>
> There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.
> 
> Here is one type of pseudocode for this coding schema:
>
> - Take a string and determine the relevant frequencies of the characters.
> - Build and sort a list of tuples from lowest to highest frequencies.
> - Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
> - Trim the Huffman Tree (remove the frequencies from the previously built tree).
> - Encode the text into its compressed form.
> - Decode the text from its compressed form.
> 
> You then will need to create encoding, decoding, and sizing schemas.

### Design Logic
- Created a node class- 'HuffmanNode' that has following properties. - char, frequency, left child and right child. 
- Created a class- 'HuffmanCoding' that include methods including huffman_encoding, huffman_decoding and all required helper methods. 
- steps for encoding and decoding
    
1. The 'build_freq_table()' method takes a string and determine the relevant frequencies of the characters store them in a dictionary, also create a HuffmanNode object of each item. 
    - Time complexity: O(n). Where n is number of character in an input string in worst case scenario, no char is repeated.
    - Space complexity: Function of 2 * n. Hence O(n)

2. Created a helper 'sort_node_list()' method. 
    - It converts Huffman node objects into tuples (char, freq, left, right) - [TC: O(n), SC: O(n)] and sorts them in rev order according to freq values- [TC: O(nlogn), SC: O(n)]
    - Convert back them into Huffman Nodes so that sorted Huffman node list returned. [TC: O(n), SC: O(n)]
    - Overall for step 2, time complexity : O(nlogn) and Space complexity is O(n)

3. The 'build_huffman_tree()' method. 
    - If node is None, return None. (Corner case)
    - If input text is just one char or repeatation of one char. create a dummy node. (corner case) 
    - Sort a node list (using step 2) and pop two nodes with lowest frequencies. Create a parent node (i.e. make the two nodes as a children of this node) with new value of freq as summantion of freqs of children.  
    - Push back parent node into sorted list. 
    - Repeat untill there is only one node remaining is a node-list
    - TC for this step would be a fuction of number of node and step 2. [i.e. O(nlogn * n].
    - SC is depends on depth of a tree. worstcase scenario depth is n. hence SC is O(n * n)

4. The 'encode()' and recursive 'encode_helper()' methods are used to encode each char according to HuffmanTree structure 
              and store them into a dictionary. 
    - TC: O(d) where d is depth of a tree and depth is n for worstcase, hence TC: O(n), 
    - SC: size of dict which is const * n. hence SC: O(n)
    - 'generate_bitsteam()' creates encoded bit stream using corresponding dictionary keys. TC- O(n), SC - const*n = O(n)
    
5. 'huffman_encoding()' method use all the helper function. 
    - TC: Overall Time complexity from step 1-4 is O(n^2.logn)
    - SC: For step 1-4 is O(n^2)
    
6. huffman_decioding()' uses reverse dictionary values to decode bitstream into a text value.
   - TC: O(n)
   - SC: O(n)

- Thus Overall Time complexity: `O(n^2.logn)` and space complexity is `O(n^2)`

- **Note**: Using inbuild priority queue data structure time complexity can be improved (as sorting could have been avoided.)
          However, I preferred using all data-structures using scratch and decided to use list and sort approach. 

