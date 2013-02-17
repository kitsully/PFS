# Kristopher Sullivan 
# Operating Systems
# February 16, 2013 

# file_name_layer

import fileLayer
import blockLayer
from fileLayer import INode, FileType
import inode_number

def createDict(data):
	b = data.split(",")
	dic = {}
	for item in b:
		part = item.split("|")
		dic.update({part[0]:part[1]})
	return dic

def string_match(filename, b):
	buf = [''] * blockLayer._block_size
	buf = b.read(0, buf, 0, b.block_size() - 1)
	d = "".join(buf)
	dic = createDict(d)
	for item in dic:
		if (filename == item):
			return True
	return False

def inode_num(filename, b):
	buf = [''] * blockLayer._block_size
	buf = b.read(0, buf, 0, b.block_size() - 1)
	d = "".join(buf)
	dic = createDict(d)
	for item in dic:
		if (filename == item):
			return int(dic.get(filename))	
	raise Exception("%s file is not in directory." % filename)


def lookup(filename, directory):
	i = inode_number.inode_number_to_inode(directory)
	if (i.inode_type != FileType.directory):
		raise Exception ("Not a directory.")
	offset = 0
	while (offset < i.size):
		b = inode_number.inode_number_to_block(offset,  directory)
		if (string_match(filename, b)):
			return inode_num(filename, b)
		offset = offset + blockLayer.get_block_size()
	raise Exception("Error")

def name_to_inode_number(filename, directory):
	return lookup(filename, directory)


if __name__ == '__main__':
	i = inode_number.inode_number_to_inode(2)	
	i.inode_type = FileType.directory
	bnum = blockLayer.get_free_block()
	# print bnum
	b = blockLayer.block_number_to_block(bnum)
	s = "Test|12,red|10"
	s = list(s)
	# print s
	b.write(0, s, 0, len(s))
	i.add_block(0, bnum)
	test = name_to_inode_number("red", 2)
	print test 

	