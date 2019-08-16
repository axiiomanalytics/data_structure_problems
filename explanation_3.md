To build a Huffman Tree for encoding and decoding, I need to use a map to store the characters and their frequencies. Then I should build a list to sort the data from highest to lowest frequencies. After that, I need to assign each character with a binary code, from shortest to longest. After the tree is built, I can use it to encode text to its compressed form and then decode the text from its compressed form.

I used sort() in huffman_encoding(data) so the time complexity is O(nlogn). The space complexity of huffman_encoding(data) is O(n). The time and space complexities of huffman_decoding(data, tree) is O(n).

reference:
http://www.openbookproject.net/py4fun/huffman/huffman.html