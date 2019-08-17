To build up a simple block chain, I used linked list to link the blocks together. Each block contains timestamp, data, SHA-256 hash code and a previous hash code. 

I append one block to the chain each time so the time complexity is O(1) while the space complexity is O(# of present blocks). 

reference:
https://medium.com/@vishnuashok123/building-a-simple-blockchain-using-python-90d27ee50214

