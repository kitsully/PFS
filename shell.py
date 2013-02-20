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

path_name_layer.chdir("/dir")

def ls(): # lists the contents of the working directory
	b = inode_number.inode_number_to_block((inode_number.inode_number_to_inode(path_name_layer._wd)).size, path_name_layer._wd)
	buf = [''] * b.size
	buf = b.read(0, buf, 0, b.size - 1)
	d = "".join(buf)
	dic = file_name_layer.createDict(d)
	for key in dic.keys():
		print "- ", key

def mkdir(directory): # creates a directory in the working directory
	file_name_layer.mkdir(directory, path_name_layer._wd)


def cd(path): # change directory 
	path_name_layer.chdir(path)






# mkdir("hello")
cd("/")
ls()
print "----"
cd("/dir")
ls()
 
