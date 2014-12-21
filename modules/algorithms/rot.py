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
		for i in range(1,26):
			print "ROT {:>2}".format(i), self.encrypt(string, i)

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
			if num > ord("z"):
				num = ord("a") + (num - ord("z")) - 1
			elif num > ord("Z") and num < ord("a"):
				num = ord("A") + (num - ord("Z")) - 1
			return chr(num)
		else:
			return char
