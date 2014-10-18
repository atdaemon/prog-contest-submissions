"""
https://www.hackerrank.com/contests/nov13/challenges/utopian-tree
"""
h = 1
d = {0:1}
for i in xrange(1,60) :
	if i%2==0 :
		h+=1
	else :
		h=h*2
	d[i] = h
#print d
T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	print d[N]

