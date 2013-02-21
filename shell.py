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


# lists the contents of the working directory
def ls():
    b = inode_number.inode_number_to_block((inode_number.inode_number_to_inode(path_name_layer._wd)).size, path_name_layer._wd)
    buf = [''] * b.size
    buf = b.read(0, buf, 0, b.size - 1)
    d = "".join(buf)
    if(0 != b.size):
        dic = file_name_layer.createDict(d)
        for key in dic.keys():
            print "- ", key
    else:
        print "Empty Directory"


# creates a directory in the working directory
def mkdir(directory): 
    file_name_layer.mkdir(directory, path_name_layer._wd)


# change directory 
def cd(path): 
    path_name_layer.chdir(path)


# Prints out the contents of a file
def cat(filename): 
    num_blocks = 0
    pointer = 0
    count = 0
    inum = file_name_layer.lookup(filename, path_name_layer._wd)
    i = inode_number.inode_number_to_inode(inum)
    for b in i.blocks:
        if (b != -1):
            num_blocks += 1 
    buf = [""] * (blockLayer._block_size * num_blocks)
    while(pointer < num_blocks):
        block = blockLayer.block_number_to_block(i.blocks[pointer])
        buf = block.read(0, buf, count, block.size)
        pointer += 1
        count += blockLayer._block_size 
    buf = "".join(buf)
    print buf 


# removes a file from a working directory
def rm(filename): 
    num = 0
    inum = file_name_layer.lookup(filename, path_name_layer._wd)
    i = inode_number.inode_number_to_inode(inum)
    for b in i.blocks:
        if (b != -1):
            blockLayer.release_block(i.blocks[num])
        num += 1
    inode_number.release_inode(inum)
    inode_directory = inode_number.inode_number_to_inode(path_name_layer._wd)
    block_directory = blockLayer.block_number_to_block(inode_directory.blocks[0])
    buf = [""] * block_directory.size
    buf = block_directory.read(0, buf, 0, block_directory.size)
    buf = "".join(buf)
    search = filename + "|" + str(inum) + ","
    buf = buf.replace(search, "")
    clear = "_" * 512
    block_directory.write(0, clear, 0, len(clear))
    block_directory.write(0, buf, 0, len(buf))
    if(len(buf) == 0): # checks to see if the directory is now empty
        block_directory.size = 0    


# removes a directory 
def rmdir(directory): 
    inum = file_name_layer.lookup(directory, path_name_layer._wd)
    i = inode_number.inode_number_to_inode(inum)
    if (i.inode_type == FileType.directory):
        blockLayer.release_block(i.blocks[0])
        inode_number.release_inode(inum)
        inode_directory = inode_number.inode_number_to_inode(path_name_layer._wd)
        block_directory = blockLayer.block_number_to_block(inode_directory.blocks[0])
        buf = [""] * block_directory.size
        buf = block_directory.read(0, buf, 0, block_directory.size)
        buf = "".join(buf)
        search = directory + "|" + str(inum) + ","
        buf = buf.replace(search, "")
        clear = "_" * 512
        block_directory.write(0, clear, 0, len(clear))
        block_directory.write(0, buf, 0, len(buf))
        if(len(buf) == 0): # checks to see if the directory is now empty
            block_directory.size = 0
    else:
        raise Exception("Inode %r is not of type directory." % inum)


# appends a string to the end of a block    
def append(filename, writer): 
    inum = file_name_layer.lookup(filename, path_name_layer._wd)
    i = inode_number.inode_number_to_inode(inum)
    bnum = i.blocks[i.size - 1]
    blk = blockLayer.block_number_to_block(bnum)
    buf = list(writer)
    b_start = 0
    while (b_start < len(buf)):
        while (blk.size < blockLayer._block_size):
            if(b_start == len(writer)):
                return 0
            buf_string = "".join(buf[b_start])
            blk.write(blk.size, buf_string, 0, 1)
            b_start += 1
        if(b_start < len(buf)):
            bnum = i.add_block()
            blk = blockLayer.block_number_to_block(bnum)


cd("/")
ls()
