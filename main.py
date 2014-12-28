from modules import *

if __name__ == "__main__":
	print "============================"
	print "      Welcome to Crypt      "
	print "============================"

	while 1:
		input = raw_input(
"""(1) MD5
(2) ROT
(3) XOR
(Anything else) Exit
""")

		if input == "1":
			md5 = MD5()
			md5.act()
		elif input == "2":
			rot = ROT()
			rot.act()
		elif input == "3":
			xor = XOR()
			xor.act()

		input = raw_input("(1) Run Again    (2) Exit\t")

		if input == "1":
			break
