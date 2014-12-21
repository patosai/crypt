from modules import *

print "Welcome to Crypt"
print "================"
input = raw_input(
"""(1) ROT
(2) XOR
(3) Another option
""")

if input == "1":
	rot = ROT()
	rot.act()
elif input == "2":
	xor = XOR()
	xor.act()
