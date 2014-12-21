def ascii_to_hex(string):
	return "".join([hex(ord(c))[2:].zfill(2) for c in string])

def hex_to_ascii(string):
	asciiString = ""
	while len(string) > 0:
		part = string[:2]
		asciiString += chr(int(part, 16))
		string = string[2:]
	return asciiString
