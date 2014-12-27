import math

# Performs frequency analysis on string, returns float from 0-1
# representing similarity to average sentence
def freqAnalysis(string):
	regRatio = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228,
	            0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
	            0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987,
	            0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
	            0.01974, 0.00074]

	string = string.replace(" ", "").lower()
	strRatio = [0.] * 26
	for char in string:
		if (char <= "z" and char >= "a"):
			strRatio[ord(char) - ord("a")] += 1
	strRatio[:] = [x/len(string) for x in strRatio]

	eucRatio = 0
	for i in range(len(regRatio)):
		eucRatio = regRatio[i]**2 + strRatio[i]**2
	eucRatio = math.sqrt(eucRatio)
	return eucRatio
