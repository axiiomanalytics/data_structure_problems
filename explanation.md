problem_1:


reference:
https://algorithms.tutorialhorizon.com/least-recently-used-lru-cache-using-hashmap-and-doubly-linked-list-set-1/
https://leetcode.com/problems/lru-cache/discuss/164037/Solution-(Python)-using-Doubly-Linked-List-and-Map-with-Detailed-Explanation


problem_2:

To find all files beneath a path with a certain suffix, I need to iterate all items under a directory. If it is a file, I will check if it has the target suffix; if it is a directory, I will use recursion to iterate its beneath items. Thus, the time complexity of find_files(suffix, path) is O(# of terminal files).

problem_3:

reference:
http://www.openbookproject.net/py4fun/huffman/huffman.html


problem_4:

To find if a user is in a group, I need to iterate through sub-groups of a group and compare target user to each user in a group.

The time complexity of is_user_in_group(user, group) is O(m*n) assumening m is the number of sub-groups and n is the number of users. The space complexity is O(1).


problem_5:

To build up a simple block chain, I used linked list to link the blocks together. Each block contains timestamp, data, SHA-256 hash code and a previous hash code. 

The time and space complexities of calc_hash() are O(1). The time and space complexities of append() are also O(1). 

reference:
https://www.ibm.com/developerworks/cloud/library/cl-develop-blockchain-app-in-python/index.html
https://medium.com/@vishnuashok123/building-a-simple-blockchain-using-python-90d27ee50214


problem_6:

To get the union or intersection of two linked lists, I need to transform them to lists first. After I get the union or intersection of the two lists, I need to transform the result to a linked list. 

The time and space complexities of to_list() are O(n) assuming n is the length of the linked list. The worst case time and space complexities of union(llinst_1, llinst_2) is O(n) assuming n is the combined size of the two linked lists. The worst case time complexity of intersection(llinst_1, llinst_2) is O(m*n) assuming m is the size of llist_1 and n is the size of llist_2. The worst case space complexity of intersection(llinst_1, llinst_2) is O(n) assuming n is the minimum size of the two linked lists.