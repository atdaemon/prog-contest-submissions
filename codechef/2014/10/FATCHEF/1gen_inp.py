T = 10
N = 100000
from random import Random
print T
for _ in xrange(T) :
	r = Random()
	M = r.randint(10000,100000)
	print N,M
	Y = sorted(Random.sample(r,xrange(1,N),M))
	for _i_ in Y :
		print chr(ord('A')+r.randint(0,25)), _i_

