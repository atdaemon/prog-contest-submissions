"""
https://www.hackerrank.com/contests/csindia/challenges/broken-keyboard
"""
T = int(raw_input())
for _ in xrange(T) :
	B = set(str(raw_input()))
	W = set(str(raw_input()))
	print len(W.intersection(B))

