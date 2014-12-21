from ..binhextool import *

class XOR:

	def act(self):
		print "XOR Cipher"
		print "----------"
		input = raw_input("(1) Encrypt ASCII    (2) Decrypt Hex\t")

		if input == "1":
			data = raw_input("Enter data: ")
			key = raw_input("Enter key: ")

			print "Output (raw): ", self.crypt(data, key, "chr")
			print "Output (hex): ", self.crypt(data, key, "hex")

		if input == "2":
			data = raw_input("Enter data: ")
			key = raw_input("Enter key: ")

			print "Output: ", self.crypt(hex_to_ascii(data), key, "chr")

	def crypt(self, string, key, type):
		cryptString = ""
		keyIndex = 0

		for x in range(len(string)):
			cryptChar = ord(string[x]) ^ ord(key[keyIndex])
			if type == "hex":
				cryptString += hex(cryptChar)[2:].zfill(2)
			elif type == "chr":
				cryptString += chr(cryptChar)
			keyIndex = (keyIndex + 1) % len(key)

		return cryptString
