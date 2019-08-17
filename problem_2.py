import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.isfile(path) :
        print('Invalid path!')
        return
    elif not os.path.exists(path):
        print('Path does not exist!')
        return
    return find_files_func(suffix, path)

def find_files_func(suffix, path):
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
            path_list += find_files_func(suffix, next_path)

    return path_list  
    

# test case 1
print('\nTest case 1: \nFind all files beneath path \"testdir_invalid\" with a suffix of \".c\". \n')
print(find_files('.c', 'testdir_invalid'))

# test case 2
print('\nTest case 2: \nFind all files beneath path \"testdir/t1.c\" with a suffix of \".c\". \n')
print(find_files('.c', 'testdir/t1.c'))

# test case 3
print('\nTest case 3: \nFind all files beneath path \"testdir_empty\" with a suffix of \".c\". \n')
print(find_files('.c', 'testdir_empty'))

# test case 4
print('\nTest case 4: \nFind all files beneath path \"testdir_empty/subdir\" with a suffix of \".c\". \n')
print(find_files('.c', 'testdir_empty/subdir'))

# test case 5
print('\nTest case 5: \nFind all files beneath path \"testdir\" with a suffix of \".c\". \n')
print(find_files('.c', 'testdir'))

# test case 6
print('\nTest case 6: \nFind all files beneath path \"testdir\" with a suffix of \".d\". \n')
print(find_files('.d', 'testdir'))

