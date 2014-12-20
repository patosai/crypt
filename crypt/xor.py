class XOR:

	def strToHex(self, string):
		hexStr = ""
		for x in string:
			hexStr = hexStr + "%02X " % ord(x)

		return hexStr

	def crypt(self, string, key):
		cryptString = ""
		keyIndex = 0

		for x in range(len(string)):
			cryptString += chr( ord(string[x]) ^ ord(key[keyIndex]))
			keyIndex = (keyIndex + 1) % len(key)

		return cryptString
