# Kristopher Sullivan 
# Operating Systems
# February 14, 2013 

# inode Number


import fileLayer
import blockLayer
from fileLayer import INode, FileType

_num_inodes = 100
_inode_table = []

for i in range(0, _num_inodes):
	_inode_table.append(INode(inode_type = FileType.regular_file))


def valid_inode(inode_num):
	return (inode_num >= 0) and (inode_num < _num_inodes)

def inode_number_to_inode(inode_num):
	if valid_inode(inode_num):
		return _inode_table[inode_num]
	else:
		raise Exception("Inode number %s out of range." % inode_num)

def inode_number_to_block(offset, inode_num):
	inode = inode_number_to_inode(inode_num)
	o = offset / blockLayer.get_block_size()
	b = inode.index_to_block_number(o)
	return blockLayer.block_number_to_block(b)



if __name__ == '__main__':
	# print _inode_table

	print "=====", _inode_table[1]
	print "=====", inode_number_to_block(512, 1)

