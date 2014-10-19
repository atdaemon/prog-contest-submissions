"""
Large input generator for problem - http://www.codechef.com/problems/SUBLCM/
"""
T = 50
N = 10**4
from random import Random
r =Random()
print T
for _ in xrange(T) :
	print N
	arr = [r.randint(1,10**6) for i in xrange(N)]
	print " ".join(map(str,arr))

