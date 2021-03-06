from ..tools import *

class ROT:

	def act(self):
		print "ROT Cipher"
		print "----------"

		input = raw_input("""(1) Encrypt
(2) Decrypt
""")

		if input == "1":
			string = raw_input("Enter your string: ")
			const = raw_input("Enter rotation constant: ")
			print "Output: ", self.encrypt(string, const)
		if input == "2":
			string = raw_input("Enter your string: ")
			self.decrypt(string)

	# decrypt rotates from 1-25, prints out everything
	def decrypt(self, string):
		# do frequency analysis
		freqList = [0.] * 25
		for i in range(1,26):
			freqList[i-1] = freqAnalysis(self.encrypt(string, i))
		# choose the lowest 10 Euc. distances
		for i in range(0,16):
			freqList[freqList.index(max(freqList))] = -1
		# display these rotations
		print "Top Ten Most Likely Rotations"
		print "-----------------------------"
		for i in range(0,25):
			if freqList[i] != -1:
				newString = self.encrypt(string, i+1)
				output = "> {:>2}: ".format(i), newString
				output = "".join(output)
				print output
				print ""

		input = raw_input("(1) See all rotations?   (Anything else) Exit\t")
		if input == "1":
			for i in range(1,26):
				newString = self.encrypt(string, i)
				output = "> {:>2}: ".format(i), newString
				output = "".join(output)
				print output
				print ""


	# encrypt rotates every character
	def encrypt(self, string, rotConst):
		try:
			const = int(rotConst)
			output = ""
			for x in string:
				output += self.rotate(x, const)
			return output;
		except ValueError:
			print "Rotate constant is not an integer"
			return "error"

	# Takes a char and an int to rotate
	def rotate(self, char, rotConst):
		if (char <= "Z" and char >= "A") or (char <= "z" and char >= "a"):
			num = ord(char) + (rotConst % 26)
			if char <= "z" and char >= "a" and num > ord("z"):
				num = ord("a") + (num - ord("z")) - 1
			elif char <= "Z" and char >= "A" and num > ord("Z"):
				num = ord("A") + (num - ord("Z")) - 1
			return chr(num)
		else:
			return char

	# Performs frequency analysis on string, returns float from 0-1
	def freqAnalysis(self, string):
		regRatio = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228,
		            0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
		            0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987,
		            0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
		            0.01974, 0.00074]

		string = string.replace(" ", "").lower()
		strRatio = [0.] * 26
		for char in string:
			if (char <= "z" and char >= "a"):
				strRatio[ord(char) - ord("a")] += 1
		strRatio[:] = [x/len(string) for x in strRatio]

		eucRatio = 0
		for i in range(len(regRatio)):
			eucRatio = regRatio[i]**2 + strRatio[i]**2
		eucRatio = math.sqrt(eucRatio)
		return eucRatio
