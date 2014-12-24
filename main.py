from modules import *

if __name__ == "__main__":
	print "============================"
	print "      Welcome to Crypt      "
	print "============================"

	while 1:
		print ""
		print "-----------------"
		print "    Main Page    "
		print "-----------------"

		input = raw_input(
"""(1) ROT
(2) XOR
(Anything else) Exit
""")

		if input == "1":
			rot = ROT()
			rot.act()
		elif input == "2":
			xor = XOR()
			xor.act()
		else:
			break
