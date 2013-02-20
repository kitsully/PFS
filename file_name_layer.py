# Kristopher Sullivan 
# Operating Systems
# February 16, 2013 

# file_name_layer

import fileLayer
import blockLayer
from fileLayer import INode, FileType
import inode_number

def createDict(data):
	b = data.split(',')
	dic = {}
	for item in b:
		part = item.split("|")
		dic.update({part[0]:part[1]})
	print "Dictionary in inode: ", dic
	return dic

def valid_filename(filename):
	return (filename.find(",") != -1) or (filename.find("|") != -1)

def string_match(filename, b):
	buf = [''] * b.size
	buf = b.read(0, buf, 0, b.size - 1)
	d = "".join(buf)
	dic = createDict(d)
	for item in dic:
		if (filename == item):
			return True
	return False

def inode_num(filename, b):
	buf = [''] * b.size
	buf = b.read(0, buf, 0, b.size - 1)
	d = "".join(buf)
	dic = createDict(d)
	for item in dic:
		if (filename == item):
			return int(dic.get(filename))	
	raise Exception("%s file is not in directory." % filename)


def lookup(filename, directory):
	if(valid_filename(filename) == 0):
		i = inode_number.inode_number_to_inode(directory)
		if (i.inode_type != FileType.directory):
			raise Exception ("Not a directory.")
		offset = 0
		while (offset < i.size):
			b = inode_number.inode_number_to_block(offset,  directory)
			if (string_match(filename, b)):
				return inode_num(filename, b)  # may need to be returned as an int
			offset = offset + blockLayer._block_size
		return 0
	else:
		raise Exception("The filename %s is not a valid name." % filename)

def name_to_inode_number(filename, directory):
	return lookup(filename, directory)


def create_file(filename, directory):
	if(valid_filename(filename) == 0):
		inum = inode_number.get_free_inode()
		i = inode_number.inode_number_to_inode(inum)
		i.inode_type=FileType.regular_file
		i.add_block()
		d_inode = inode_number.inode_number_to_inode(directory)
		d_block = inode_number.inode_number_to_block((d_inode.size - 1) * blockLayer._block_size, directory)
		data = filename + "|" + str(inum) + ","
		d_block.write(d_block.size, data, 0, len(data))
		b_string = [""] * d_block.size
		b_string = d_block.read(0, b_string, 0, d_block.size)

def mkdir(filename, directory):
		inum = inode_number.get_free_inode()
		i = inode_number.inode_number_to_inode(inum)
		i.inode_type = FileType.directory
		i.add_block()
		d_inode = inode_number.inode_number_to_inode(directory)
		d_block = inode_number.inode_number_to_block((d_inode.size - 1) * blockLayer._block_size, directory)
		data = filename + "|" + str(inum) + ","
		d_block.write(d_block.size, data, 0, len(data))
		b_string = [""] * d_block.size
		b_string = d_block.read(0, b_string, 0, d_block.size)



# if __name__ == '__main__':

	# create_file("test", 0)
	# create_file(2, 2)

	# i = inode_number.get_free_inode()
	# i = inode_number.inode_number_to_inode(i)
	# i.inode_type = FileType.directory
	# i.blocks[0] = blockLayer.get_free_block()
	# bnum = i.blocks[0]
	# block = blockLayer.block_number_to_block(bnum)
	# s = "test|1"
	# s = list(s)
	# block.write(0, s, 0, len(s))

	#print lookup("telll", 2)

	# i = inode_number.inode_number_to_inode(2)	
	# i.inode_type = FileType.directory
	# bnum = blockLayer.get_free_block()
	# print bnum
	# b = blockLayer.block_number_to_block(bnum)
	# s = "Test|12,red|10"
	# s = list(s)
	# print s
	# b.write(0, s, 0, len(s))
	# i.add_block(0, bnum)
	# test = lookup("red", 2)
	# print test 

	