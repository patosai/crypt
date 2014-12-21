from modules import *

print "Welcome to Crypt"
print "================"
input = raw_input(
"""(1) XOR
(2) Another option
""")

if input == "1":
	xor = XOR()
	xor.act()
