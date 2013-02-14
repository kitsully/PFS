# Kristopher Sullivan 
# Operating Systems
# February 14, 2013 

# inode Number


import fileLayer
from fileLayer import INode, FileType

_num_inodes = 100
_inode_table = []

for i in range(0, _num_inodes):
	_inode_table.append(INode(inode_type = FileType.regular_file))


if __name__ == '__main__':
	print _inode_table