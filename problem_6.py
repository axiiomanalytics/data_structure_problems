class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def to_list(self):
        """
        Transform the linked list to a list
        """
        ls = []
        node = self.head
        while node:
            ls.append(node.value)
            node = node.next
        
        return ls

def union(llist_1, llist_2):
    """
    Return the union of two linked lists. A union is a set of elements which are in llist_1, in llist_2 or in both 
    llist_1 and llist_2. Values of llist_1 and llist_2 are unique values.
    """
    # if one or both linked lists are empty
    if llist_1.head is None:
        if llist_2.head is None:
            return None
        else:
            return llist_2
    
    elif llist_1.head and llist_2.head is None:
        return llist_1
    
    # transform the linked list to a list
    list_1 = llist_1.to_list()
    list_2 = llist_2.to_list()
    
    # get the union of list_1 and list_2
    union_ls = set(list_1 + list_2)
    
    # transform union_ls to a linked list
    union = LinkedList()
    for element in union_ls:
        union.append(element)
        
    return union

def intersection(llist_1, llist_2):
    """
    Return the intersection of two linked lists. An intersection is a set of elements which are in both llist_1 and 
    in llist_2. Values of llist_1 and llist_2 are unique values.
    """
    # if one or both linked lists are empty
    if llist_1.head is None or llist_2.head is None:
        return None
    
    # transform the linked list to a list
    list_1 = llist_1.to_list()
    list_2 = llist_2.to_list()
    
    # get the intersection of list_1 and list_2
    inter_ls = []
    for element in list_1:
        if element in list_2:
            inter_ls.append(element)
    
    # transform inter_ls to a linked list
    inter = LinkedList()
    for element in inter_ls:
        inter.append(element)
        
    return inter
    
    

# test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('Case 1 result:')
print (union(linked_list_1,linked_list_2)) # return None
print (intersection(linked_list_1,linked_list_2)) # return None

# test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [1, 2, 3]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print('\nCase 2 result:')
print (union(linked_list_3,linked_list_4)) # return 1 -> 2 -> 3 ->
print (intersection(linked_list_3,linked_list_4)) # return None

# test case 3
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1, 2, 3]
element_2 = [3, 4, 5]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('\nCase 3 result:')
print (union(linked_list_1,linked_list_2)) # return 1 -> 2 -> 3 -> 4 -> 5 ->
print (intersection(linked_list_1,linked_list_2)) # return 3 ->