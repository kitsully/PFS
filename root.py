import fileLayer
import blockLayer
from fileLayer import INode, FileType
import inode_number
import file_name_layer

inode_number._inode_table[0].add_block()
print inode_number._inode_table[0].blocks
# inode_number._inode_table[1].add_block()
# print inode_number._inode_table[1]
# print inode_number._inode_table[1].blocks



file_name_layer.create_file("wooo", 0)
file_name_layer.create_file("FUCKYES", 0)
# file_name_layer.create_file("FUCKYES", 1)


b = file_name_layer.lookup("wooo", 0)

print b

#b1 = Block_Layer.block_number_to_block(inode_table[0].blocks[0])

#print b1

#print file_name_layer.lookup("wooo", 0)