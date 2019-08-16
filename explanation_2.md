To find all files beneath a path with a certain suffix, I need to iterate all items under a directory. If it is a file, I will check if it has the target suffix; if it is a directory, I will use recursion to iterate its beneath items. 

The time complexity of find_files(suffix, path) is O(# of all terminal files). The space complexity is O(# of all target files).

