# Kristopher Sullivan 
# Operating Systems
# February 16, 2013 

# file_name_layer

import fileLayer
import blockLayer
from fileLayer import INode, FileType
import inode_number




def lookup(filename, directory):
	i = INode() 
	i = inode_number_to_inode(directory)
	if (i.inode_type != FileType.directory):
		raise Exception ("Not a directory.")
	offset = 0
	while (offset < i.size):
		b = blockLayer.inode_number_to_block(offset,  directory)
		if (string_match(filename, b):
			return inode_number(filename, b)
		offset = offset + blockLayer.get_block_size()
	raise Exception("Error")

def createDict(data):
	b = data.split(",")
	dic = {}
	l = []
	for item in b:
		part = item.split("|")
		dic.update({part[0]:part[1]})
	return dic

def string_match(filename, b):
	buf = [''] * blockLayer._block_size
	buf = b.read(0, buf, 0, b.max_capacity)
	d = "".join(buf)
	dic = createDict(d)
	for item in dic:
		if (filename == item):
			return True
		else:
			return False

def inode_num(filename, b):
	buf = [''] * blockLayer._block_size
	buf = b.read(0, buf, 0, b.max_capacity)
	d = "".join(buf)
	dic = createDict(d)
	for item in dic:
		if (filename == item):
			print dic.get(filename)
		else:
			raise Exception("%s file is not in directory." % filename)


# c = blockLayer.Block()
# s = "Test|12,red|10"
# c.write(0, s, 0, len(s))
# inode_number("Test", c)

