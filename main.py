from crypt import *
from binhextool import *

xor = XOR()

print "Welcome to Crypt"
print "================"
print ""

xor = XOR()
print "XOR Cipher"
print "----------------"
input = raw_input("(1) Encrypt ASCII\t(2) Decrypt Hex\t")

if input == "1":
	data = raw_input("Enter data: ")
	key = raw_input("Enter key: ")

	print "Output (raw): ", xor.crypt(data, key, "chr")
	print "Output (bin): ", xor.crypt(data, key, "bin")
	print "Output (hex): ", xor.crypt(data, key, "hex")

if input == "2":
	data = raw_input("Enter data: ")
	key = raw_input("Enter key: ")

	print "Output: ", xor.crypt(hex_to_ascii(data), key, "chr")
