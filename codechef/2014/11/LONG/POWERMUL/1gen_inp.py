T = 100
print T
from random import Random
Random = Random()
totalN = 10**4
totalQ = 10**4
for _ in xrange(T) :
	N = 2
	if totalN > 2 : N = Random.randint(2,totalN)
	totalN-=N
	M = Random.randint(1,10**9-1)
	Q = 2 
	if totalQ > 2 : Q = Random.randint(2,totalQ) 
	totalQ-=Q
	print N,M,Q
	for __ in xrange(Q) :
		r = Random.randint(1,N-1)
		print r

