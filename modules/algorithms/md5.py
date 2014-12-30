import hashlib

class MD5:
	def act(self):
		filePath = raw_input("Enter filepath: ")

		print "MD5 checksum: ", self.getChecksum(filePath)

	def getChecksum(self, filePath):
		with open(filePath, 'rb') as handle:
			m = hashlib.md5()
			while True:
				data = handle.read(8192)
				if not data:
					break
				m.update(data)
			return m.hexdigest()
