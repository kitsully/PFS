# Kristopher Sullivan 
# Operating Systems
# February 7, 2013 

# Block Layer

from array import array

data = []

class Block:
	size = 512
	buff = buffer(" ", 0, 0)
	def write(self, block_start, buff1, buffer_start, num_bytes):
		if (num_bytes < 512):
			buff = buffer(buff1, buffer_start, num_bytes)
			print buff
		else:
			print "error"
		return 0


	def read(block_start, buffer, buffer_start, num_bytes):
		print "Test"
		return 0


	def block_size(self):
		print "hello"
		return self.block_size


b = Block()





# Example of how to write to a block
b.write(0, "Hello World", 7, 511)
