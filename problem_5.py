import hashlib
from datetime import datetime

class Block():
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()
    
    def __repr__(self):
        return f'Timestamp: {str(self.timestamp)}\nData: {str(self.data)}\nSHA256 Hash: {str(self.hash)}\nPrevious_Hash: {str(self.previous_hash)}'
    
class BlockChain():
    """
    Build up a simple block chain using linked list.
    """
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, timestamp, data):
        # if the blockchain is empty, make the new block as the head
        if self.head is None:
            self.head = Block(timestamp, data, 0)
            self.tail = self.head
        else:
            # use previous_hash to link the new block
            previous_hash = self.tail.hash
            self.tail = Block(timestamp, data, previous_hash)
            self.tail.previous_hash = previous_hash
            
            
            
# test case 1
print('Test case 1:')
blockchain = BlockChain()
print('Blockchain is empty.')
print(blockchain.head)

# test case 2
print('\nTest case 2:')
print('\nAdd Block One:')
blockchain.append(datetime.utcnow(), 'Block One')
print(blockchain.tail)

# test case 3
print('\nTest case 3:')
print('\nAdd Block Two:')
blockchain.append(datetime.utcnow(), 'Block Two')
print(blockchain.tail)

# test case 4
print('\nTest case 4:')
print('\nAdd another three blocks:')
blockchain.append(datetime.utcnow(), 'Block Three')
print(f'\n{blockchain.tail}')
blockchain.append(datetime.utcnow(), 'Block Four')
print(f'\n{blockchain.tail}')
blockchain.append(datetime.utcnow(), 'Block Five')
print(f'\n{blockchain.tail}')