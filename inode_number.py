# Kristopher Sullivan 
# Operating Systems
# February 14, 2013 

# inode Number


import fileLayer
import blockLayer
from fileLayer import INode, FileType

_num_inodes = 100
_inode_table = []
_free_inodes = [0] * _num_inodes




for i in range(0, _num_inodes):
	_inode_table.append(INode(inode_type = FileType.regular_file))

def release_inode(num):
    if(_free_inodes[num] == 0):  # checks if free
        print "Already Free"
    else: 
        _free_inodes[num] = 0  # Changes inode status to free 

def get_free_inode():
    for i in range(0, _inode_table - 1): 
        if(_free_inodes[i] == 0): 
            _free_inodes[i] = 1  # Block No Longer Free 
            return i
        else: 
            raise Exception("No more free inodes.")

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
    inode = INode()
    inode.add_block(0, 32)
    print inode
    _inode_table[0] = inode
    print _inode_table[0]
    
    test = inode_number_to_block(0, 0)
    print test


