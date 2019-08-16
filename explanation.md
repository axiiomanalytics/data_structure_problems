problem_1:

I want to create a LRU cache to store values. Every time when I add a new value to the cache, it will become the head. Every time when I check an existing value, it will move to the head as the most recently used value and the tail is the least recently used value. If the cache is full, I will delete the tail and then add the new value. Considered the time complexity of O(1), an appropriate data structure should be doubly linked list. I use map and doubly linked list to maintain the structure of LRU cache: the head stores the node with the most recently used key and the tail stores the node with the least recently used key.

reference:
https://algorithms.tutorialhorizon.com/least-recently-used-lru-cache-using-hashmap-and-doubly-linked-list-set-1/


problem_2:

To find all files beneath a path with a certain suffix, I need to iterate all items under a directory. If it is a file, I will check if it has the target suffix; if it is a directory, I will use recursion to iterate its beneath items. 

The time complexity of find_files(suffix, path) is O(# of all terminal files). The space complexity is O(# of all target files).


problem_3:

To build a Huffman Tree for encoding and decoding, I need to use a map to store the characters and their frequencies. Then I should build a list to sort the data from highest to lowest frequencies. After that, I need to assign each character with a binary code, from shortest to longest. After the tree is built, I can use it to encode text to its compressed form and then decode the text from its compressed form.

I used sort() in huffman_encoding(data) so the time complexity is O(nlogn). The space complexity of huffman_encoding(data) is O(n). The time and space complexities of huffman_decoding(data, tree) is O(n).

reference:
http://www.openbookproject.net/py4fun/huffman/huffman.html


problem_4:

To find if a user is in a group, I need to iterate through sub-groups of a group and compare target user to each user in a group.

The time complexity of is_user_in_group(user, group) is O(m*n) in which m is the number of sub-groups and n is the number of users. The space complexity is O(n).


problem_5:

To build up a simple block chain, I used linked list to link the blocks together. Each block contains timestamp, data, SHA-256 hash code and a previous hash code. 

The time and space complexities of calc_hash() are O(1). The time and space complexities of append() are also O(1). 

reference:
https://www.ibm.com/developerworks/cloud/library/cl-develop-blockchain-app-in-python/index.html
https://medium.com/@vishnuashok123/building-a-simple-blockchain-using-python-90d27ee50214


problem_6:

To get the union or intersection of two linked lists, I need to transform them to lists first. After I get the union or intersection of the two lists, I need to transform the result to a linked list. 

The time and space complexities of to_list() are O(n) in which n is the length of the linked list. The worst case time and space complexities of union(llinst_1, llinst_2) is O(n) in which n is the combined size of the two linked lists. The worst case time complexity of intersection(llinst_1, llinst_2) is O(m*n) in which m is the size of llist_1 and n is the size of llist_2. The worst case space complexity of intersection(llinst_1, llinst_2) is O(n) in which n is the minimum size of the two linked lists.