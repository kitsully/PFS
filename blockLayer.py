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
		for i in range(block_start, block_start + num_bytes):
			if (self.blk[buf_i] != ""):
				buff1 += self.blk[buf_i] #
				i += 1
				buf_i += 1
		return buff1


	# Prints the entire block for testing purposes
	def print_block_content(self):
		print self.blk
		return None 


b = Block()



r = ""


# Example of how to write to a block
b.write(0, "Hello Worl", 0, 10) 
# b.block_size() # this prints out the whole list the first few spaces should be equal to hello world


s = "I think I did it!"
#b.write(35, s, 0, 17)

r = b.read(0, r, 2, 10)

print r


#b.print_block_content()
