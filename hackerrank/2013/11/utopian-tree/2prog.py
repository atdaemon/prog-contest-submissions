"""
https://www.hackerrank.com/challenges/utopian-tree
"""
T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	height = 1
	for i in xrange(N) :
		if i%2 == 0 :
			height = height*2
		else :
			height += 1
	print height

