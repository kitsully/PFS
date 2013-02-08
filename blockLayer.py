# Kristopher Sullivan 
# Operating Systems
# February 7, 2013 

# Block Layer

class Block:
	size = 512
	blk = ["0"] * 512
	def write(self, block_start, buff1, buffer_start, num_bytes):
		buf_i = buffer_start
		for i in range(block_start, block_start + num_bytes):
			n = i
			if (n < len(buff1)):
				self.blk[i] = buff1[n]
			i += 1
		return 0


	def read(block_start, buffer, buffer_start, num_bytes):
		print "Test"
		return 0


	def block_size(self):
		print self.blk
		return self.block_size


b = Block()





# Example of how to write to a block
b.write(0, "Hello World", 0, 511)
b.block_size()
