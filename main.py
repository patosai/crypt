from crypt import *

keyStr = "this is a key"
testStr = "The quick brown fox jumps over the lazy dog"

xor = XOR()

print xor.strToHex(xor.Crypt(testStr, keyStr))
