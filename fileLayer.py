# Kristopher Sullivan 
# Operating Systems
# February 13, 2013 

# File Layer

import blockLayer


class iNode:
	max_number_blocks_per_file = 100  # the max number of blocks per file
	iNode = ['_'] * max_number_blocks_per_file  # the list holding the files data in sequence
	size = 0  # the maximum size of the iNode

	# Procedures ------

	def index_to_block_number(self, index):
		return self.iNode[index]

