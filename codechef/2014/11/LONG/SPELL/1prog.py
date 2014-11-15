"""
http://www.codechef.com/NOV14/problems/SPELL
#trivial solution
"""
import sys

def lineGetter() :
	with sys.stdin as inp :
		for line in inp :
			yield line.strip()

getLine = lineGetter()
N = getLine.next()
N = int(N)

for _ in xrange(N) :
	getLine.next()
print getLine.next()
