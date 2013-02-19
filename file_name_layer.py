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
	print b
	for item in b:
		part = item.split("|")
		dic.update({part[0]:part[1]})
	print dic
	return dic

def valid_filename(filename):
	return (filename.find(",") != -1) or (filename.find("|") != -1)

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
	print directory
	if(valid_filename(filename) == 0):
		i = inode_number.inode_number_to_inode(directory)
		if (i.inode_type != FileType.directory):
			raise Exception ("Not a directory.")
		offset = 0
		while (offset < i.size):
			b = inode_number.inode_number_to_block(offset,  directory)
			if (string_match(filename, b)):
				return inode_num(filename, b)  # may need to be returned as an int
			offset = offset + blockLayer.get_block_size()
		raise Exception("Error")
	else:
		raise Exception("The filename %s is not a valid name." % filename)

def name_to_inode_number(filename, directory):
	return lookup(filename, directory)


def create_file(filename, directory):
	if(valid_filename(filename) == 0):
		inum = inode_number.get_free_inode()
		i = INode(inode_type = FileType.regular_file)
		bnum = i.add_block()
		block = blockLayer.block_number_to_block(bnum)
		d_inode = inode_number.inode_number_to_inode(directory)
		d_block = inode_number.inode_number_to_block((d_inode.size - 1) * blockLayer._block_size, directory)
		print "#####", d_block
		data = filename + "|" + str(inum) + ","
		d_block.write(d_block.size - 1, data, 0, len(data))
		b_string = [""] * d_block.size
		b_string = d_block.read(0, b_string, 0, d_block.size)
		print b_string

# def create_file(file_name, direct):
#     if(valid_file_name(file_name) == 0):
#         inode_num = InodeNumber_Layer.get_free_inode()
#         inode = Inode(inode_type=FileType.regular_file)
#         block_num = inode.add_block()
#         block = Block_Layer.block_number_to_block(block_num)
#         direct_inode = InodeNumber_Layer.inode_number_to_inode(direct)
#         direct_block = InodeNumber_Layer.inode_number_to_block((direct_inode.size-1)*Block_Layer.block_size, direct)
#         string = file_name+"|"+str(inode_num)+","
#         direct_block.write(direct_block.size, string, 0, len(string))
#         block_string = [""] * direct_block.size
#         block_string = direct_block.read(0, block_string, 0, direct_block.size)
#         print direct_block.block[0:512]


# def create_file(file_name, direct):
#     if(valid_file_name(file_name) == 0):
#         inode_num = InodeNumber_Layer.get_free_inode()
#         inode = Inode(inode_type=FileType.regular_file)
#         block_num = inode.add_block()
#         block = Block_Layer.block_number_to_block(block_num)
#         direct_inode = InodeNumber_Layer.inode_number_to_inode(direct)
#         direct_block = InodeNumber_Layer.inode_number_to_block((direct_inode.size-1)*Block_Layer.block_size, direct)
#         string = file_name+"|"+str(inode_num)+","
#         direct_block.write(direct_block.size, string, 0, len(string))
#         block_string = [""] * direct_block.size
#         block_string = direct_block.read(0, block_string, 0, direct_block.size)



		# inum = inode_number.get_free_inode()
		# i = inode_number.inode_number_to_inode(inum)
		# i.inode_type = FileType.regular_file
		# #print "$$$$$", blockLayer.get_free_block()
		# #print "$$$$$", blockLayer.get_free_block()
		# i.blocks[0] = blockLayer.get_free_block()
		# #print "@@@@@", i.blocks[0]
		# bnum = i.blocks[0]
		# block = blockLayer.block_number_to_block(bnum)
		# i_direct = inode_number.inode_number_to_inode(directory)
		# i_direct.blocks[0] = blockLayer.get_free_block()
		# #print "!!!!!!!", i_direct.blocks[0]
		# block_direct = inode_number.inode_number_to_block((i_direct.size - 1) * blockLayer.get_block_size(), directory)
 	# 	d = filename + "|" + str(inum) + ","
 	# 	block_direct.write(block_direct.size, d, 0, len(d))
 	# 	string = [""] * block_direct.size
 	# 	string = block_direct.read(0, string, 0, block_direct.size)
 	# 	print string

		# i3 = inode_number.get_free_inode()
		# i2 = inode_number.inode_number_to_inode(i3)
		# i2.blocks[0] = blockLayer.get_free_block()
		# i2.inode_type = FileType.directory
		# bnum2 = i2.blocks[0]
		# block2 = blockLayer.block_number_to_block(bnum2)
		# d = directory + "|" + str(i1) + ","
		# block2.write(0, d, 0, len(d))
		# r = [""] * 20
		# r = block2.read(0, r, 0, 20)
		# print r










if __name__ == '__main__':

	create_file("test", 0)
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

	