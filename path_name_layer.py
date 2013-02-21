# Kristopher Sullivan 
# Operating Systems
# February 17, 2013 

# path_name

import file_name_layer

global _wd # global variable to hold the working directory 
_wd = 0


# scans its argument for the UNIX path name separator (forward slash).
def plain_name(path): 
    if (path.find("/") == -1):
        return True
    else:
        return False


# returns the first component name
def first(path): 
    loc = path.split("/")
    return loc[0]


# returns the remainder of the path name
def rest(path): 
    loc = path.split("/", 1)
    return loc[1]


# takes a path its inode number
def path_to_inode_number(path, directory): 
    if (plain_name(path)):
        return file_name_layer.name_to_inode_number(path, directory)
    else:
        directory = file_name_layer.lookup(first(path), directory)
        path = rest(path)
        return path_to_inode_number(path, directory)


# changes the working directory 
def chdir(path): 
    global _wd
    if (path == "/"):
        global _wd
        _wd = 0
        return 1 #success
    elif(path[0] == "/"):
        global _wd
        _wd = path_to_inode_number(path[1:], 0)
        return 1
    global _wd 
    _wd = path_to_inode_number(path, _wd)
    return 1



#if __name__ == '__main__':
    # global _wd
    # _wd = 12
    # print "----", _wd 
    # i = inode_number.inode_number_to_inode(2) 
    # i.inode_type = FileType.directory
    # p = "right/wrong/left"
    # test 

