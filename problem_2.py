import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories and those subdirectories may also contain further 
    subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path is None:
        return None
    
    path_list = []
    if os.path.isfile(path):
        if path.endswith(suffix):
            path_list.append(path)
            
    elif os.path.isdir(path):
        dir_list = os.listdir(path)
        for item in dir_list:
            next_path = os.path.join(path, item)
            path_list += find_files(suffix, next_path)
            
    return path_list  
    


# test case
print('Test case: \nFind all files with a suffix of \".c\" beneath folder testdir. \n')
print(find_files('.c', 'testdir'))