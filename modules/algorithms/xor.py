from ..binhextool import *

class XOR:

	def act(self):
		print "XOR Cipher"
		print "----------"
		input = raw_input(
		"""(1) Encrypt ASCII (plaintext & key)
(2) Decrypt Hex (ciphertext & key)
(3) Get the key (plaintext & ciphertext)
""")

		if input == "3":
			plain = raw_input("Plaintext: ")
			cipher = raw_input("Ciphertext: ")
			repeatKey = self.crypt(hex_to_ascii(cipher), plain, "chr")
			print "Repeating Key XOR: ", repeatKey
			print "Key? : ", self.getKey(repeatKey)
		else:
			data = raw_input("Enter data: ")
			key = raw_input("Enter key: ")

			if input == "1":
				print "Output (raw): ", self.crypt(data, key, "chr")
				print "Output (hex): ", self.crypt(data, key, "hex")

				if input == "2":
					print "Output: ", self.crypt(hex_to_ascii(data), key, "chr")

	# crypt takes in an ASCII string and xor's it with the key
	# "Type" indicates whether output will be hex or ASCII
	def crypt(self, string, key, type):
		cryptString = ""
		keyIndex = 0

		for x in string:
			cryptChar = ord(x) ^ ord(key[keyIndex])
			if type == "chr":
				cryptString += chr(cryptChar)
			elif type == "hex":
				cryptString += hex(cryptChar)[2:].zfill(2)

			keyIndex = (keyIndex + 1) % len(key)

		return cryptString

	# given a repeating key xor, will attempt to find the key
	def getKey(self, string):
		key = ""
		for i in range(1, len(string)):
			index = string.replace(string[0:i], " "*len(string[0:i]), 1).find(string[0:i])
			if index > -1:
				key = string[0:index]
		return key
