# Kristopher Sullivan 
# Operating Systems
# February 13, 2013 

# File Layer

import blockLayer


_num_blocks_in_file = 100


# c = blockLayer.get_free_block()

# c.set_size(400)
# print c.block_size()



class FileType(object):
	regular_file = 1
	directory = 2
		



class INode(object):
	def __init__(self, inode_type = FileType.regular_file):
		self.blocks = _num_blocks_in_file * [-1] # the max number of blocks per file
		self.size = 0
		self.inode_type = inode_type
	


	# iNode = ['_'] * max_number_blocks_per_file  # the list holding the files data in sequence
	# size = 0  # the maximum size of the iNode

	# Procedures ------

	# def index_to_block_number(self, index):
	# 	return self.iNode[index]

	# def inode_to_block(self, byte_offset):
	# 	o = byte_offset / c.block_size()
	# 	b = self.index_to_block_number(o)
	# 	return c.block_number_to_block(b)



if __name__ == '__main__':
	inode = INode()
	print inode.blocks
	print inode.size
	print inode.inode_type





# node = INode()

# print node.inode_to_block(30)
