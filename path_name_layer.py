# Kristopher Sullivan 
# Operating Systems
# February 17, 2013 

# path_name

import fileLayer
import blockLayer
from fileLayer import INode, FileType
import inode_number
import file_name_layer

def plain_name(path): # scans its argument for the UNIX path name separator (forward slash).
	if (path.find("/") == -1):
		return True
	else:
		return True

def first(path): # returns the first component name
	loc = path.find("/")
	return path[:loc]
	# print loc

def rest(path): # returns the remainder of the path name
	loc = path.find("/")
	return path[loc:]

def path_to_inode_number(path, directory):
	if (plain_name(path)):
		return file_name_layer.name_to_inode_number(path, directory)
	else:
		directory = file_name_layer.lookup(first(path), directory)
		path = rest(path)
		return path_to_inode_number(path, directory)