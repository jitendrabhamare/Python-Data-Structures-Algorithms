import sys

class HuffmanNode(object):
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


class HuffmanCoding(object):
    def __init__(self):
        self.code_map = {}
        self.rev_code_map = {}

    def build_freq_table(self, data):
        """ Build a dict table char and freq
            Create Huffman nodes for each item
        """
        
        # Build char-freq table
        freq_table = {}
        for c in data:
            if freq_table.get(c) is None:
                freq_table[c] = 1
            else:
                freq_table[c] += 1

        # Create HuffmanNode list
        node_list = []
        for key in freq_table:
            node = HuffmanNode(key, freq_table[key])
            node_list.append(node)

        return node_list

    def sort_node_list(self, node_list):
        """ Convert Huffman node objects into tuples (char, freq, left, right)
            Sort them in rev order according to freq values
            COnvert back them into Huffman Nodes so that sorted Huffman node list returned
        """
        
        # Convert HuffmanNode DS intu tuple list and sort in rev order according to freq
        tup_list = [(item.char, item.freq, item.left, item.right) for item in node_list]
        tup_list = sorted(tup_list, key=lambda a: a[1], reverse=True)

        # Corvert back tuple_list into node_list
        sorted_node_list = []
        for tup in tup_list:
            node = HuffmanNode(*tup)
            sorted_node_list.append(node)

        return sorted_node_list


    def build_huffman_tree(self, node_list):
        """ Core algorithm of Huffman encoding - 
            Build the Huffman Tree by assigning a binary code to each letter, 
            using shorter codes for the more frequent letters.
        """
        if node_list is None:
            return None
        
        # Create a dummy node for corner case - 
        # when input text is just one char (Ex. "a" or "aaa")?
        if len(node_list) == 1:
            dummy_node = HuffmanNode("\0", 0)
            node_list.append(dummy_node)

        while len(node_list) > 1:
            node_list = self.sort_node_list(node_list)
            #for node in node_list:
                #print(node.char, node.freq, node.left, node.right)
            node1 = node_list.pop()
            node2 = node_list.pop()
            parent = HuffmanNode(None, node1.freq + node2.freq, node1, node2)
            #print("\nparent: ({}, {}, {}, {})".format(parent.char, parent.freq, parent.left, parent.right))
            node_list.append(parent)

        return node_list

    def encode(self, root):
        current_code = ""
        self.encode_helper(root, current_code)
        #print("code_map: {}".format(self.code_map))

    def encode_helper(self, node, current_code):
        if node is None:
            return None

        if node.char is not None:
            self.code_map[node.char] = current_code

        self.encode_helper(node.left, current_code + "0")
        self.encode_helper(node.right, current_code + "1")

    def generate_bitstream(self, data):
        bs = ""
        for c in data:
            bs += self.code_map[c]
        
        return bs

    def huffman_encoding(self, data):

        if data == "":
            raise ValueError("Please specify a non-empty input text") 
        # Get a sorted frequency table 
        freq_table = self.build_freq_table(data)
        #print("freq_table: {}".format(freq_table))

        # Build a tree and get a root 
        trimmed_list = self.build_huffman_tree(freq_table)
        root = trimmed_list[0]

        # Encode data into Huffman-tree
        self.encode(root)

        # Generate a bitstream 
        bitstream = self.generate_bitstream(data)
        #print(bitstream)

        return bitstream, root
                

    def huffman_decoding(self, data, tree):
        self.rev_code_map = {v:k for k, v in self.code_map.items()}
        #print("rev_dict: {}".format(self.rev_code_map))
        decoded_text = ""
        encoded_char = ""

        for bit in data:
            encoded_char += bit

            if encoded_char in self.rev_code_map:
                decoded_text += self.rev_code_map[encoded_char]
                encoded_char = ""

        return decoded_text


if __name__ == "__main__":
    codes = {}

    ## Following Five test-cases are specified in a list. 
    ## Last testcase should raise a value Error.

    sentence_list = ["The bird is the word", "a", "aaaaa", "abracadabra", ""]
    count = 1
    print("______________________________________________________________________")
    for a_great_sentence in sentence_list:
        print("test-case - {}".format(count))
        print("______________________________________________________________________")
        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))
      
        a = HuffmanCoding()
        encoded_data, tree = a.huffman_encoding(a_great_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = a.huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
        print("______________________________________________________________________")
        count += 1





