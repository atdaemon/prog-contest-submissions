"""
http://www.codechef.com/JUNE14/problems/MAXPRa
#here's the inefficient v1.0
"""

from itertools import combinations

MOD = 10**9+7
T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	A = map(int,raw_input().split())
	#print T,N,A
	ans=pow(2,N,MOD)
	#for 0 , 1 , 2 length sequences
	ans=(ans-1-N-N*(N-1)/2)%MOD
	# for 3 to N
	for size in xrange(3,N+1) :
		#print "size = ", size
		combs = len(filter(lambda x:x,[all((i - j) == (j - k) for i, j, k in zip(l[:-2], l[1:-1], l[2:])) for l in combinations(A,size)]))
		#print "combinations =",combs
		ans=(ans-combs)%MOD
	print ans

