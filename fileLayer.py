# Kristopher Sullivan 
# Operating Systems
# February 13, 2013 

# File Layer

import block

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
        return True

    def index_to_block_number(self, index):
        if self.valid_index(index):
            return self.blocks[index]
        raise Exception("Index number %s out of range." % index)

if __name__ == '__main__':
    print "File inode:"
    inode = INode()
    print inode.blocks
    print inode.size
    print inode.inode_type

    print "Directory inode:"
    inode = INode(inode_type=FileType.directory)
    print inode.blocks
    print inode.size
    print inode.inode_type
