import hashlib

class MD5:
	def act(self):
		input = raw_input("Enter string to hash: ")
		print "Output: ", hashlib.md5(input).hexdigest()
