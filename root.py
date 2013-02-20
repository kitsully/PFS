import fileLayer
import blockLayer
from fileLayer import INode, FileType
import inode_number
import file_name_layer
import path_name_layer

inode_number._inode_table[0].add_block()


file_name_layer.mkdir("dir", 0)
d_inode = path_name_layer.path_to_inode_number("dir", 0)
print "dir", d_inode
file_name_layer.create_file("wooo", d_inode)
file_name_layer.create_file("FUCKYES", d_inode)
file_name_layer.mkdir("dir2", d_inode)
d_inode2 = path_name_layer.path_to_inode_number("dir2", d_inode)
print "dir2", d_inode2

path_name_layer.chdir("/")
print path_name_layer._wd

path_name_layer.chdir("/dir")
print path_name_layer._wd




path_name_layer.chdir("/dir/dir2")
#print path_name_layer._wd

#path_name_layer.chdir("/dir2")

#print inode_number._free_inodes[0:]

# d_inode = path_name_layer.path_to_inode_number("dir", 0)
# print "--", d_inode

# inode_number._inode_table[1].add_block()
# print inode_number._inode_table[1]
# print inode_number._inode_table[1].blocks



# file_name_layer.create_file("wooo", 0)
# file_name_layer.create_file("FUCKYES", 0)

# file_name_layer.create_file("FUCKYES", 1)


# b = file_name_layer.lookup("FUCKYES", 0)

# print _wd

#b1 = Block_Layer.block_number_to_block(inode_table[0].blocks[0])

#print b1

#print file_name_layer.lookup("wooo", 0)