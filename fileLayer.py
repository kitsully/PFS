# Kristopher Sullivan 
# Operating Systems
# February 13, 2013 

# File Layer

import blockLayer

_num_blocks_in_file = 100

class FileType(object):
    regular_file = 1
    directory = 2

class INode(object):
    def __init__(self, inode_type=FileType.regular_file):
        self.blocks = _num_blocks_in_file * [-1]
        self.size = 0
        self.inode_type = inode_type
        
    def valid_index(self, index):
        print "*****", self.blocks[index]
        if (index >= 0 and index <= _num_blocks_in_file - 1 and self.blocks[index] != -1):
        	return True
        else:
            raise Exception("%r at %r not a valid index" % (self.blocks[index], index))	

    def add_block(self):
    	index = self.size
        self.blocks[index] = blockLayer.get_free_block()
        self.size += 1
        return self.blocks[index]

    def index_to_block_number(self, index):
        if self.valid_index(index):
            return self.blocks[index]
        else:
        	raise Exception("Index number %s out of range." % index)

    def inode_to_block(self, byte_offset):
    	o = byte_offset / blockLayer.get_block_size()
    	b = self.index_to_block_number(o)
    	return blockLayer.block_number_to_block(b)


# if __name__ == '__main__':
    # print "File inode:"
    # inode = INode()
    # b = blockLayer.Block()
    # inode.add_block(1, 32)
    # print inode.index_to_block_number(1)
    # print inode.inode_to_block(514)
    # print inode.blocks
    # print inode.size
    # print inode.inode_type

    # print "Directory inode:"
    # inode = INode(inode_type=FileType.directory)
    # print inode.blocks
    # print inode.size
    # print inode.inode_type
