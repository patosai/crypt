class XOR:

	def crypt(self, string, key, type):
		cryptString = ""
		keyIndex = 0

		for x in range(len(string)):
			cryptChar = ord(string[x]) ^ ord(key[keyIndex])
			if type == "bin":
				cryptString += bin(cryptChar) + " "
			elif type == "hex":
				cryptString += hex(cryptChar)[2:].zfill(2)
			elif type == "chr":
				cryptString += chr(cryptChar)
			keyIndex = (keyIndex + 1) % len(key)

		return cryptString
