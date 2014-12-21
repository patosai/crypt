from modules import *

print "Welcome to Crypt"
print "================"
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
