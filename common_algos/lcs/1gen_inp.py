"""
N = input string size
Generates two random strings of length N
"""
N = 800
from random import Random
import sys,os
r = Random()

def getchar() :
	return chr(ord('a') + r.randint(0,25))

base = ord('a')
out = sys.stdout
for i in xrange(N) : out.write(getchar())
out.write(os.linesep)
r = Random()
for i in xrange(N) : out.write(getchar())
out.flush()



