# Kristopher Sullivan 
# Operating Systems
# February 7, 2013 

# Block Layer

device_size = 1000

#device = [""] * 1000  # device with 1000 blocks
free_list = [0] * device_size  # a list holding the status of the block free or used

# free_list[5] = 1







class Block:
	size = 0
	max_capacity = 512
	blk = ['_'] * 512  # This creates a list with 512 spaces 
	def write(self, block_start, buff1, buffer_start, num_bytes):
		buf_i = buffer_start 
		for i in range(block_start, block_start + num_bytes): 
			# checks if block can be written too
			if(i < self.max_capacity):
				self.blk[i] = buff1[buf_i]
			else:
				self.size = i + 1
				return 1 # failure if full text was not written
			# Checks for index out of bound problem
			if(buf_i <= num_bytes): 
				buf_i += 1
			else:
				self.size = i + 1
				return 0 # success
			i += 1
		self.size = i + 1
		return 1 # return failure by default


	def read(self, block_start, buff1, buffer_start, num_bytes):
		if ((block_start + num_bytes) > self.max_capacity):
			return 1 # Failure	
		for i in range(block_start, block_start + num_bytes):
			buff1[buffer_start] = self.blk[i]
			i += 1
			buffer_start += 1 
		return buff1 # returns what has been read in from the block


	"""Returns the size of the block"""
	def block_size(self):
		return self.size


	"""Sets the max_capacity of the clock"""
	def set_size(self, s):
		self.max_capacity = s


	"""This method prints out the entire contents of the bock for testing purposes."""
	def print_block_content(self):
		print self.blk
		return None 


"""Finds a free block in the device"""
def get_free_block():
    for i in range(0, 0 + device_size-1): 
        if(free_list[i] == 0): 
            free_list[i] = 1 
            return i
    return 1 #failure


"""Sets a blocks status to free"""
def release_block(num):
    if(free_list[num] == 0):#checks if free
        print "Already Free"
    else: 
        free_list[num] = 1 


def block_number_to_block(num):
	return device[num]

# def make_device(size):
# 	device = [] * size
# 	print device
# 	for i in range(size - 1):
# 		b = Block()
# 		device[1] = b
# 		print i
# 		#i = i + 1
# 	return device

device = [Block() for i in range(device_size - 1)]

block_num = get_free_block()
b = block_number_to_block(block_num)

r = [""] * b.max_capacity # an array with the same size as a block. Will be used to read
s = "I think I did it!"
b.write(0, s, 0, 17)
s2 = "change" 
b.write(4, s2, 2, 4)
r = b.read(0, r, 0, b.max_capacity)
print r

release_block(block_num)
block_num = get_free_block()
b = block_number_to_block(block_num)
r = [""] * b.max_capacity
s3 = "I released the block and changed it!" 
b.write(0, s3, 0, len(s3)-1)
r = b.read(0, r, 0, b.max_capacity)
print r

# b = Block() # instantiates a block 

# r = "" # declares a string to hold data read from block
# s = "I think I did it!"
# b.write(35, s, 0, 17)

# r = [""] * len(s)
#print get_free_block()

# Example of how to write to a block
# b.write(0, "Hello Worl", 0, 10) # writes Hello Worl to the block 
# b.print_block_content()
# r = b.read(35, r, 0, len(s)) # reads the content of the block starting at the second character



# print r

# print b.block_size() # prints the data that was read 


