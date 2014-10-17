"""
Large input generator for - 
http://www.codechef.com/OCT14/problems/CHEFSQUA
"""
N = 2000
print N
from random import Random
r = Random()
X = r.sample(xrange(-10**6,10**6),N)
Y = r.sample(xrange(-10**6,10**6),N)
for x,y in zip(X,Y) :
	print x,y

