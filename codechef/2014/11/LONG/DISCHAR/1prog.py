"""
http://www.codechef.com/NOV14/problems/DISCHAR
"""

T = int(raw_input())
for _ in xrange(T) :
	s = set()
	for c in str(raw_input()) : s.add(c)
	print len(s)

