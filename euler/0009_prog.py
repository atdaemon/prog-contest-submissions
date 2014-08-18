"""
https://projecteuler.net/problem=9
https://www.hackerrank.com/contests/projecteuler/challenges/euler009
"""
import math
squares = set([x**2 for x in xrange(1,3001)])
ans = [-1]*3001
for a in xrange(1,3000) :
	for b in xrange(a+1,3001-a) :
		c2 = a**2 + b**2
		if c2 not in squares : continue
		c = int(math.sqrt(c2))
		if a+b+c> 3000 : break
		N = a+b+c
		ans[N] = max(ans[N],a*b*c)
	#	print a+b+c,a,b,c,a*b*c
#print ans
T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	print ans[N]

