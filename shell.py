# Kristopher Sullivan
# Operating Systems
# February 19, 2013

# Shell Module

import fileLayer
import blockLayer
from fileLayer import INode, FileType
import inode_number
import file_name_layer
import path_name_layer
import absolute_path_name_layer


def ls(): # lists the contents of the working directory
	b = inode_number.inode_number_to_block((inode_number.inode_number_to_inode(path_name_layer._wd)).size, path_name_layer._wd)
	buf = [''] * b.size
	buf = b.read(0, buf, 0, b.size - 1)
	d = "".join(buf)
	if(0 != b.size):
		dic = file_name_layer.createDict(d)
		for key in dic.keys():
			print "- ", key
	else:
		print "Empty Directory"

def mkdir(directory): # creates a directory in the working directory
	file_name_layer.mkdir(directory, path_name_layer._wd)


def cd(path): # change directory 
	path_name_layer.chdir(path)


def cat(filename): # Prints out the contents of a file
	num_blocks = 0
	pointer = 0
	count = 0
	inum = file_name_layer.lookup(filename, path_name_layer._wd)
	i = inode_number.inode_number_to_inode(inum)
	for b in i.blocks:
		if (b != -1):
			num_blocks += 1
	# print "-----", num_blocks		
	buf = [""] * (blockLayer._block_size * num_blocks)
	while(pointer < num_blocks):
		block = blockLayer.block_number_to_block(i.blocks[pointer])
		# s = "dfdfdfdfd"
		# block.write(0, s, 0, len(s) )
		buf = block.read(0, buf, count, block.size)
		pointer += 1
		count += blockLayer._block_size 
	buf = "".join(buf)
	print buf
 



# cd("/")
# ls()
# print "----"
# cd("/Home/Kris/Music")
cd("/Home/Kris/Docs")
cat("Doc_1")
# ls()
 
