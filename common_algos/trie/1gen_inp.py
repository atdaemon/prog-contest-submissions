"""
Generate random strings to be inserted into the trie
N = max length of string
M = number of strings
only lower case letters for now

author : @atdaemon

"""
from random import Random
N = 100
M = 100
r = Random()
charA = ord('a')
print M
for _ in xrange(M) :
	n = r.randint(1,N)
	letters = r.sample(xrange(N*10),n)
	letters = "".join([chr(charA+(letter%26)) for letter in letters])
	print letters

