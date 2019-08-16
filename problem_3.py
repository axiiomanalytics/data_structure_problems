import sys

def huffman_encoding(data):
    """
    This function takes a text string as input and returns the encoded data and a tree with characters and binary codes.
    """
    # take a string and determine the relevant frequencies of the characters
    freq_dict = {}
    for char in data:
        if char not in freq_dict:
            freq_dict[char] = 1
        else: 
            freq_dict[char] += 1
    
    # build and sort a list of tuples from highest to lowest frequencies
    freq_ls = []
    for key, value in freq_dict.items():
        tuple = value, key
        freq_ls.append(tuple) # value first for sorting
        
    sorted_freq = sorted(freq_ls, reverse=True)

    # build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters
    tree = {}
    code = '1'
    for item in sorted_freq:
        char = item[1]
        tree[char] = code
        code = '0' + code
    
    # encode the text into its compressed form
    encode = ''
    for char in data:
        encode += tree[char]
        
    return encode, tree


# decode the text from its compressed form
def huffman_decoding(data, tree):
    """
    This function takes binary data and a tree of codes as input and returns the decoded data.
    """
    new_tree = {}
    for key, value in tree.items():
        new_tree[value] = key
        
    decode = ''
    code = ''
    for bit in data:
        if bit == '1':
            decode += new_tree[code + bit]
            code = '' # reset code 
        else:
            code += bit
    


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