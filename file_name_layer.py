# Kristopher Sullivan 
# Operating Systems
# February 16, 2013 

# file_name_layer

import fileLayer
import blockLayer
from fileLayer import INode, FileType
import inode_number

# _wd = ""  # the working directory


def lookup(filename, directory):
	i = INode() 
	i = inode_number_to_inode(directory)
	if (i.inode_type != FileType.directory):
		raise Exception ("Not a directory.")
	offset = 0
	while offset < i.size:
		b = blockLayer.inode_number_to_block(offset,  directory)
		if (string_match(filename, b):
			return inode_number(filename, b)
		offset = offset + blockLayer.get_block_size()
	raise Exception("Error")


def createDict(data):
	data = test.split(",")
	dic = {}
	l = []
	for item in b:
		part = item.split("|")
		dic.update({part[0]:part[1]})
	return dic