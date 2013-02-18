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


def general_path_to_inode_number(path):
	path.strip("/")
	if (path[0] == "/"):
		return path_to_inode_number(path, 1)
	else:
		return path_to_inode_number(path, wd)