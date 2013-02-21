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

#Creates the directories
inode_number._inode_table[0].add_block()

# Creates home directory and adds a few files
file_name_layer.mkdir("Home", 0)
d_inode = path_name_layer.path_to_inode_number("Home", 0)
file_name_layer.create_file("test_1", d_inode)
file_name_layer.create_file("test_2", d_inode)
file_name_layer.create_file("test_3", d_inode)
file_name_layer.create_file("test_4", d_inode)

# Creates Kris directory
file_name_layer.mkdir("Kris", d_inode)
d_inode2 = path_name_layer.path_to_inode_number("Kris", d_inode)

# Creates Docs directory
file_name_layer.mkdir("Docs", d_inode2)
d_inode_docs = path_name_layer.path_to_inode_number("Docs", d_inode2)
file_name_layer.create_file("Doc_1", d_inode_docs) # I want to write to this file
inum = path_name_layer.path_to_inode_number("Doc_1", d_inode_docs)
i = inode_number.inode_number_to_inode(inum)
block = blockLayer.block_number_to_block(i.blocks[0])
s = "Testing 1... 2... 3... 4.... 5... 6.... 7...."
block.write(0, s, 0, len(s))

# Creates Pics directory
file_name_layer.mkdir("Pics", d_inode2)
d_inode_pics = path_name_layer.path_to_inode_number("Pics", d_inode2)
file_name_layer.create_file("img_1", d_inode_pics)
file_name_layer.create_file("img_2", d_inode_pics)

# Creates Music directory
file_name_layer.mkdir("Music", d_inode2)
d_inode_music = path_name_layer.path_to_inode_number("Music", d_inode2)
file_name_layer.create_file("song_1", d_inode_music)
file_name_layer.create_file("song_2", d_inode_music)

# Create an empty directory
file_name_layer.mkdir("Empty", d_inode2)
d_inode_music = path_name_layer.path_to_inode_number("Empty", d_inode2)


def general_path_to_inode_number(path):
	path.strip("/")
	# print "path: ", path
	if (path[0] == "/"):
		return path_name_layer.path_to_inode_number(path, 0)
	else:
		return path_name_layer.path_to_inode_number(path, path_name_layer._wd)