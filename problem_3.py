import sys

class Node():   
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Node({self.get_value()})"


# take a string and determine the relevant frequencies of the characters
# build and sort a list of tuples from lowest to highest frequencies
def sortedFreq(string):
    """
    This function takes a text string as input and returns a sorted list of tuples (frequency, letter).
    """
    freq_dict = {}
    for letter in string:
        if letter not in freq_dict:
            freq_dict[letter] = 1
        else: 
            freq_dict[letter] += 1
            
    freq_ls = []
    for key, value in freq_dict.items():
        freq_ls.append(value, key) # value first for sorting
        
    sorted_freq = sorted(freq_ls)
    
    return sorted_freq


# build the Huffman Tree 
def buildTree(sorted_freq):
    """
    This function takes a sorted frequency list and returns the Huffman Tree.  
    """
    while len(sorted_freq) > 1:
        # take the first 2 letters (least frequent) and remove them from the list
        least = tuple(sorted_freq[0:2]) # make it a tuple
        rest_ls = sorted_freq[2:]

        # sum the frequency of the first 2 letters as branch point and add it to the frequency list
        sum_freq = least[0][0] + least[1][0]
        rest_ls.append((sum_freq, least))
        rest_ls.sort()

    tree = rest_ls[0] 
    
    return tree

    
# trim the Huffman Tree (remove the frequencies)
def trimTree(tree):
    """
    This function takes the Huffman Tree and remove the frequencies.
    """
    branch = tree[1]
    if type(branch) == type(''): # if branch is a leaf
        return branch
    else: # if not a leaf, trim left then right and then combine
        new_tree = (trimTree(branch[0]), trimTree(branch[1]))
    
    return new_tree
    
    
# assign a binary code to each letter
def assignCode(tree, code=''):
    """
    This function assigns a binary code to each letter. 
    """
    global codes
    if type(tree) == type(''): # if tree is a leaf
        codes[tree] = code
    else:
        assignCode(tree[0], code+'0') # plus 0 on left branch
        assignCode(tree[1], code+'1') # plus 1 on right branch
    
      
# encode the text into its compressed form
def huffman_encoding(data):
    global codes
    output = ''
    for letter in data:
        output += codes[letter]
    
    return output


# decode the text from its compressed form
def huffman_decoding(data, tree):
    output = ''
    branch = tree
    for bit in data:
        if bit == '0': # go to left branch
            branch = tree[0]
        else: # go to right branch
            branch = tree[1]
        
        if type(branch) == type(''):
            output += branch
            branch = tree
    return output
    


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))