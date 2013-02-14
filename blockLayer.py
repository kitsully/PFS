# Kristopher Sullivan 
# Operating Systems
# February 7, 2013 

# Block Layer

device_size = 10000
free_list = [0] * device_size  # a list holding the status of the block free or used


class Block(object):
    def __init__(self):
        self.size = 0
        self.max_capacity = 512
        self.blk = ['_'] * 512

    """Write from a buffer to a specific location in a block"""
    def write(self, block_start, buff1, buffer_start, num_bytes):
        buf_i = buffer_start 
        for i in range(block_start, block_start + num_bytes): 
            # checks if block can be written too
            if(i < self.max_capacity):
                self.blk[i] = buff1[buf_i]
            else:
                self.size = i + 1
                raise Exception("Full text not written")
            # Checks for index out of bound problem
            if(buf_i <= num_bytes): 
                buf_i += 1
            else:
                self.size = i + 1
                return 0  # success
            i += 1
        self.size = i + 1
        return 0  

    """Read from a specific location in a block into a buffer"""
    def read(self, block_start, buff1, buffer_start, num_bytes):
        if ((block_start + num_bytes) > self.max_capacity):  # Checks to see if trying to read more than block can hold
            raise Exception("Attempting to read more bytes than in block") 
        for i in range(block_start, block_start + num_bytes):
            buff1[buffer_start] = self.blk[i]
            i += 1
            buffer_start += 1 
        return buff1  # returns what has been read in from the block

    """Returns the size of the block"""
    def block_size(self):
        return self.size

    """Sets the max_capacity of the block"""
    def set_size(self, s):
        self.max_capacity = s


"""Finds a free block in the device Allocates a free block""" 
def get_free_block():
    for i in range(0, device_size - 1): 
        if(free_list[i] == 0): 
            free_list[i] = 1  # Block No Longer Free 
            return i
        else: 
            raise Exception("No more free blocks.")


"""Sets a blocks status to free"""
def release_block(num):
    if(free_list[num] == 0):  # checks if free
        print "Already Free"
    else: 
        free_list[num] = 0  # Changes Block status to free 


device = [Block() for i in range(device_size - 1)]  # a device with 1000 blocks


"""Returns the Block at this location in the device"""
def block_number_to_block(num):
    if (0 <= num) and (num < device_size):
        return device[num]
    else:
        raise Exception("Out of Range")



if __name__ == '__main__':
    print "----------"
    # print "Free blocks", free_list[:100]
    # block_num = get_free_block()
    # b = block_number_to_block(block_num)

    # r = [""] * b.max_capacity # an array with the same size as a block. Will be used to read
    # s = "I think I did it!"
    # b.write(0, s, 0, 17)
    # s2 = "change" 
    # b.write(4, s2, 2, 4)
    # r = b.read(0, r, 0, b.max_capacity)
    # print r

    # release_block(block_num)
    # block_num = get_free_block()
    # b = block_number_to_block(block_num)
    # r = [""] * b.max_capacity
    # s3 = "I released the block and changed it!" 
    # b.write(0, s3, 0, len(s3) - 1)
    # r = b.read(0, r, 0, b.max_capacity)
    # print r

# b = Block()
# print "s", b.block_size()












