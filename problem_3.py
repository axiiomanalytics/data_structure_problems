import sys

def huffman_encoding(data):
    """
    This function takes a string as input and returns the encoded data and a tree with characters and binary codes.
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
    if data is None:
        return None
    
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
    
    return decode
    

def test_code(data):
    if data is '':
        print('No message to compress.\n')
        return
    
    elif type(data) != type(''):
        print('String message only.\n')
        return
        
    else:
        print (f'\nThe size of the data is: {sys.getsizeof(data)}\n')
        print (f'The content of the data is: {data}\n')

        encoded_data, tree = huffman_encoding(data)
        print (f'The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}\n')
        print (f'The content of the encoded data is: {encoded_data}\n')

        decoded_data = huffman_decoding(encoded_data, tree)
        print (f'The size of the decoded data is: {sys.getsizeof(decoded_data)}\n')
        print (f'The content of the decoded data is: {decoded_data}\n') 

        
# test case 1
print('\nTest case 1: compress message \"\".\n')
data = ''
test_code(data)

# test case 2
print('\nTest case 2: compress message 23.\n')
data = 23
test_code(data)

# test case 3
print('\nTest case 3: compress message \"aaa\".')
data = 'aaa'
test_code(data)

# test case 4
print('\nTest case 4: compress message \"hello\".')
data = 'hello'
test_code(data)

# test case 5
print('\nTest case 5: compress message \"The bird is the word.\".')
data = 'The bird is the word.'
test_code(data)
           
            