# Kristopher Sullivan 
# Operating Systems
# February 7, 2013 

# Block Layer

class Block:
	size = 512
	blk = buffer(" ", 0, 0)
	def write(self, block_start, buff1, buffer_start, num_bytes):
		if (num_bytes < self.size):
			buff = buffer(buff1, buffer_start, num_bytes)
			self.blk = buffer(buff1, block_start, self.size)
			#print self.blk
		else:
			print "error"
		return 0


	def read(block_start, buffer, buffer_start, num_bytes):
		print "Test"
		return 0


	def block_size(self):
		print self.blk
		return self.block_size


b = Block()





# Example of how to write to a block
b.write(0, "Hello World", 7, 511)
b.block_size()
