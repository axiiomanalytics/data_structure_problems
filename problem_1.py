# create a class of Doubly Linked List
class Node():    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None
               
    def __repr__(self):
        return f'{self.value}'
        
        
class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        """
        Utilizes map and doubly linked list to maintain the structure of LRU cache: the head stores the node 
        with the most recently used key and the tail stores the node with the least recently used key.
        """
        if capacity <= 0:
            print ('Capacity should be greater than 0.')
            return
        
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None
        
    def size(self):
        return len(self.cache)
      
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache:
            return -1
        else: 
            current = self.cache[key]
            # if it is head, return its value
            if current is self.head:
                return current.value
            # if it is tail, set new tail
            elif current is self.tail:
                self.tail = current.previous
            # if it is in the middle, update pointers
            else:
                current.previous.next = current.next
                current.next.previous = current.previous

            # set new head
            self.head.previous = current
            current.next = self.head
            self.head = current
            return self.head.value
        
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache:
            return
        else:
            # create a new node
            node = Node(key, value)
            
            # if cache is empty
            if self.size() == 0:
                self.cache[key] = node
                self.head = node
                self.tail = self.head
            
            else:
                # if cache if full
                if self.size() == self.capacity:
                    del self.cache[self.tail.key] # delete the tail key (least recently used key)
                    
                self.cache[key] = node # add the new key
                self.head.previous = node # set the new node as head
                node.next = self.head 
                self.head = node
        print(f'cache: {self.cache}')
        
            
            
# test case 1
print('Test case 1: \nSet capacity as 0')
our_cache = LRU_Cache(0)

# test case 2
print('\nTest case 2: \nSet capacity as 1')
our_cache = LRU_Cache(1)
print('\nAdd 1 to cache')
our_cache.set(1, 1)

print('\nGet 1 from cache')
print(our_cache.get(1)) 

print('\nAdd 2 to cache')
our_cache.set(2, 2)

print('\nGet 2 from cache')
print(our_cache.get(2)) 

# test case 3
print('\nTest case 2: \nSet capacity as 5')
our_cache = LRU_Cache(5)

print('\nAdd 1 to cache')
our_cache.set(1, 1);
print('\nAdd 2 to cache')
our_cache.set(2, 2);
print('\nAdd 3 to cache')
our_cache.set(3, 3);
print('\nAdd 4 to cache')
our_cache.set(4, 4);

print('\nGet 1 from cache')
print(our_cache.get(1)) 
print('\nGet 2 from cache')
print(our_cache.get(2)) 
print('\nGet 9 from cache')
print(our_cache.get(9)) 

print('\nAdd 5 to cache')
our_cache.set(5, 5) 
print('\nAdd 6 to cache')
our_cache.set(6, 6)

print('\nGet 6 from cache')
print(our_cache.get(6))
print('\nGet 3 from cache')
print(our_cache.get(3))
