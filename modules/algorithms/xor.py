from ..tools import *
from collections import Counter
from itertools import izip, cycle

class XOR:

	def act(self):
		print "XOR Cipher"
		print "----------"
		#print getHammingDistance("100", "101")

		input = raw_input(
		"""(1) Encrypt ASCII (plaintext & key)
(2) Decrypt Hex (ciphertext & key)
(3) Get the key (plaintext & ciphertext)
(4) Attempt to break hex ciphertext
""")

		if input == "3":
			plain = raw_input("Plaintext: ")
			cipher = raw_input("Ciphertext: ")
			repeatKey = self.crypt(hex2string(cipher), plain, "chr")
			print "Repeating Key XOR: ", repeatKey
			print "Key? : ", self.getKey(repeatKey)
		elif input == "4":
			cipher = raw_input("Ciphertext: ")
			self.crack(cipher)
		else:
			data = raw_input("Enter data: ")
			key = raw_input("Enter key: ")

			if input == "1":
				#print "Output (raw): ", self.crypt(data, key, "chr")
				print "Output (hex): ", self.crypt(data, key, "hex")

			if input == "2":
				print "Output: ", self.crypt(hex2string(data), key, "chr")

	# crypt takes in an ASCII string and xor's it with the key
	# "Type" indicates whether output will be hex or ASCII
	def crypt(self, string, key, type):
		cryptString = ""
		keyIndex = 0

		for x in range(len(string)):
			cryptChar = ord(string[x]) ^ ord(key[x % len(key)])
			if type == "chr":
				cryptString += chr(cryptChar)
			elif type == "hex":
				cryptString += hex(cryptChar)[2:].zfill(2)

		return cryptString

	# given a repeating key xor, will attempt to find the key
	def getKey(self, string):
		key = ""
		for i in range(1, len(string)):
			index = string.replace(string[0:i], " "*len(string[0:i]), 1).find(string[0:i])
			if index > -1:
				key = string[0:index]
		if key != "":
			temp = self.getKey(key)
			if temp != "":
				key = self.getKey(key)
		return key

#################### DECRYPTION ###################
	def decrypt(self, c_num, k_num):
		return ''.join(chr(c ^ k) for c, k in izip(c_num, cycle(k_num)))

	def shift(self, data, offset):
		return data[offset:] + data[:offset]

	def count_same(self, a, b):
		count = 0
		for x, y in zip(a, b):
			if x == y:
				count += 1
		return count

	# String is ciphertext, key is one character
	# Gives back "score", the higher, the more likely the character is part
	# of the key
	def getDecryptScore(self, string, key):
		letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		nums = "1234567890"
		puncs = ".,'\"/?`~"

		decrypted = ''.join(chr(ord(s) ^ ord(key)) for s in string)
		score = 0
		for x in decrypted:
			if letters.find(x) != -1:
				score += 20
			elif nums.find(x) != -1:
				score += 10
			elif puncs.find(x) != -1:
				score += 2

		return score

	# string is hex, attempts to crack
	def crack(self, string):
		enc_ascii = string.decode('hex')

		enc_numbers = [ord(ch) for ch in enc_ascii]

		frequencies = [0] * 20

		print (' Len Count Rel. Freq.')
		# TODO: probably need to change range
		for key_len in range(1, 20): # try multiple key lengths
			freq = self.count_same(enc_numbers, self.shift(enc_numbers, key_len))
			frequencies[key_len] = freq
			print ('{0:< 3d} | {1:3d} |'.format(key_len, freq) + '=' * (freq / 4))

		# find key length
		key_len = frequencies.index(max(frequencies))
		# find alt key length
		alt_freqs = list(frequencies)
		alt_freqs[alt_freqs.index(max(alt_freqs))] = 0
		alt_key_len = alt_freqs.index(max(alt_freqs))

		if key_len % alt_key_len == 0:
			key_len = alt_key_len
		print "Key length is probably", key_len

		# now with key length determined, we can start guessing the key
		printable = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,'\"/?`~"

		key = []

		for i in range(1,key_len + 1):
			#keeps track of scores of all characters in printable
			scores = []
