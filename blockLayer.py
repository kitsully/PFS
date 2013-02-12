# Kristopher Sullivan 
# Operating Systems
# February 7, 2013 

# Block Layer

class Block:
	size = 512
	blk = [""] * 512  # This creates a list with 512 spaces 
	def write(self, block_start, buff1, buffer_start, num_bytes):
		buf_i = buffer_start 
		for i in range(block_start, block_start + num_bytes): 
			# checks if block can be written too
			if(i < self.size):
				self.blk[i] = buff1[buf_i]
			else:
				return 1 # failure if full text was not written
			# Checks for index out of bound problem
			if(buf_i < num_bytes): 
				buf_i += 1
			else:
				return 0 # success
			i += 1
		return 1 # return failure by default


	def read(self, block_start, buff1, buffer_start, num_bytes):
		buf_i = buffer_start
		if (num_bytes < self.size):
			for i in range(block_start, block_start + num_bytes):
				if (self.blk[buf_i] != ""): # checks to make sure the spot in block isn't empty see change on line 9
					buff1 += self.blk[buf_i] # appends the character in the block to the string
					i += 1
					buf_i += 1
		else:
			return buff1   
		return buff1 # returns what has been read in from the block


	"""Returns the size of the block"""
	def block_size(self):
		return self.size


	"""Sets the size of the clock"""
	def set_size(self, s):
		self.size = s


	"""This method prints out the entire contents of the bock for testing purposes."""
	def print_block_content(self):
		print self.blk
		return None 


b = Block() # instantiates a block 

# r = "" # declares a string to hold data read from block


# Example of how to write to a block
# b.write(0, "Hello Worl", 0, 10) # writes Hello Worl to the block 
# s = "I think I did it!"
# b.write(35, s, 0, 17)

# r = b.read(0, r, 2, 511) # reads the content of the block starting at the second character

b.set_size(3)
print b.block_size() # prints the data that was read 


