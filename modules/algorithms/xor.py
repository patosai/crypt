from ..tools import *
from collections import Counter
from fractions import gcd
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
	# Shifts a string a certain 'offset' distance
	def shift(self, data, offset):
		return data[offset:] + data[:offset]

	# Counts number of same characters in strings a and b
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
		puncs = ".,:;'\"/?~`!@#$%^&*()-+="

		decrypted = ''.join(chr(ord(s) ^ ord(key)) for s in string)
		score = 0
		for x in decrypted:
			if x == ' ':
				score += 20
			elif letters.find(x) != -1:
				score += 8
			elif nums.find(x) != -1:
				score += 4
			elif puncs.find(x) != -1:
				score += 1
			else:
				score -= 50

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
		freq_avg = sum(frequencies[1:])/(len(frequencies)-1.0)
		key_len = 0
		for i in range(1,len(frequencies)):
			if frequencies[i] > freq_avg:
				key_len = i
				break

		while (1):
			print "Key length is probably", key_len
			input = raw_input("Key length override (optional): ")
			if input != "":
				key_len = ord(input) - ord("0")
			else:
				break

		# now with key length determined, we can start guessing the key
		printable = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_ "

		key = []

		for i in range(0,key_len):
			#keeps track of scores of all characters in printable
			scores = [0] * len(printable)
			substr = ""
			# get ith, 2ith, 3ith.... chars and sent to getDecryptScore function
			for j in range(0, len(enc_ascii), key_len):
				if (j*key_len) + i < len(enc_ascii):
					substr += enc_ascii[j + i]
			for j in range(len(printable)):
				scores[j] = self.getDecryptScore(substr, printable[j])

			indexOfHighestScore = scores.index(max(scores))
			key.append(printable[indexOfHighestScore])

		print "I think the key is","".join(key)
		print ""

		print "Decrypting:"
		print self.crypt(enc_ascii, "".join(key), "chr")
