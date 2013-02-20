# Kristopher Sullivan 
# Operating Systems
# February 17, 2013 

# path_name

import fileLayer
import blockLayer
from fileLayer import INode, FileType
import inode_number
import file_name_layer

global _wd
_wd = 0

def plain_name(path): # scans its argument for the UNIX path name separator (forward slash).
	if (path.find("/") == -1):
		return True
	else:
		return False

def first(path): # returns the first component name
	loc = path.split("/")
	return loc[0]

def rest(path): # returns the remainder of the path name
	loc = path.split("/", 1)
	return loc[1]

def path_to_inode_number(path, directory): # takes a path its inode number
	if (plain_name(path)):
		print "path: ", path
		return file_name_layer.name_to_inode_number(path, directory)
	else:
		print "path: ", path
		directory = file_name_layer.lookup(first(path), directory)
		path = rest(path)
		return path_to_inode_number(path, directory)

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

