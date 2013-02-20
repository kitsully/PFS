# Kristopher Sullivan 
# Operating Systems
# February 17, 2013 

# absolute path name layer 

import fileLayer
import blockLayer
from fileLayer import INode, FileType
import inode_number
import file_name_layer
import path_name_layer
from path_name_layer import _wd

inode_number._inode_table[0].add_block()

file_name_layer.mkdir("dir", 0)
d_inode = path_name_layer.path_to_inode_number("dir", 0)
file_name_layer.create_file("wooo", d_inode)
file_name_layer.create_file("FUCKYES", d_inode)
file_name_layer.mkdir("dir2", d_inode)
d_inode2 = path_name_layer.path_to_inode_number("dir2", d_inode)
file_name_layer.mkdir("dir3", d_inode2)
d_inode3 = path_name_layer.path_to_inode_number("dir3", d_inode2)


# path_name_layer.chdir("/")
# print path_name_layer._wd

# path_name_layer.chdir("/dir")
# print path_name_layer._wd

# test = path_name_layer.chdir("/dir/dir2/dir3")
# print test


def general_path_to_inode_number(path):
	path.strip("/")
	print "path: ", path
	if (path[0] == "/"):
		return path_name_layer.path_to_inode_number(path, 0)
	else:
		return path_name_layer.path_to_inode_number(path, path_name_layer._wd)


print "wd:", path_name_layer._wd
test = general_path_to_inode_number("/dir/dir2/dir3")
print test