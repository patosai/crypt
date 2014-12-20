from crypt import *

xor = XOR()

#print xor.strToHex(xor.Crypt(testStr, keyStr))

print "Welcome to Crypt"
print "================"
print ""

xor = XOR()
print "XOR Cipher"
print "----------------"

data = raw_input("Enter data: ")
key = raw_input("Enter key: ")

output = xor.crypt(data, key)

print "Output (reg): ", output
print "Output (hex): ", xor.strToHex(output)
