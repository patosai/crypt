def string2bin(s):
	return [ord(x) for x in s]

def bin2string(b):
	return ''.join(chr(x) for x in b)

def string2hex(s):
	return s.encode('hex')

def hex2string(s):
	return s.decode('hex')

def bin2hex(b):
	return string2hex(bin2string(b))

def hex2bin(s):
	return string2bin(hex2string(s))
