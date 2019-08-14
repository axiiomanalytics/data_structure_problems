# create a class of Doubly Linked List
class Node():
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        """
        Utilizes HashMap and Doubly Linked List to maintain the structure of LRU cache: the head stores the Node 
        with the most recently used key and the tail stores the Node with the least recently used key.
        """
        if capacity <= 0:
            print ('LRU_Cache capacity should be greater than 0.')
            return
        
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None
        self.size = 0
    
    def use_node(self, node):
        # if node is head, do nothing
        if node is self.head:
            return
        # if node is tail, set a new tail
        elif node is self.tail:
            self.tail = self.tail.previous
        else:
            # if node.next is not none, create new connection
            if node.next:
                node.next.previous = node.previous
            # if node.previous is not none, create new connection
            if node.previous:
                node.previous.next = node.next
                
        # set a new head
        self.head.previous = node
        node.next = self.head
        self.head = node
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            self.use_node(self.cache[key])
            value = self.cache[key].value
            return value
        else:
            return -1
            
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            self.use_node(self.cache[key])
            self.cache[key].value = value
        else:
            # create a new node
            node = Node(key, value)
            self.cache[key] = node
            
            # if it's the first node
            if self.size == 0:
                self.head = node
                self.tail = node
            
            if self.size < self.capacity:
                self.size += 1
                
            # if cache is full
            if self.size == self.capacity:
                tail_key = self.tail.key
                if self.size == 1:
                    self.head = node
                    self.tail = node
                else:
                    self.tail = self.tail.previous
                # delete old tail
                del self.cache[tail_key]
            self.use_node(node) 
            
            
            
# test case 1
our_cache = LRU_Cache(0)

# test case 2
our_cache = LRU_Cache(1)

our_cache.set(1, 1)
print(our_cache.get(1)) # return 1

our_cache.set(2, 2)
print(our_cache.get(2)) # return 2

# test case 3
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print(our_cache.get(1)) # return 1
print(our_cache.get(2)) # return 2
print(our_cache.get(9)) # return -1

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(6)) # return 6
print(our_cache.get(3)) # return -1