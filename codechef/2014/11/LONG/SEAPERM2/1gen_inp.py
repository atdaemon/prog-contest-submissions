"""
Vary TMax : 1<= T <= 10
Vary NMax : 3 <= N <= 300
"""
TMax = 10
NMax = 20
from random import Random
r = Random()
T = r.randint(1,TMax)
T = TMax
print T
for _ in xrange(T) :
	N = r.randint(3,NMax)
	print N
	#generate a random N length list
	L = r.sample(xrange(1,N+1),N)
	L2 = [" ".join(map(str,[(j-1 if j>L[i] else j) for j in L[:i]+L[i+1:]])) for i in xrange(N)]
	r.shuffle(L2)
	print "\n".join(L2)

