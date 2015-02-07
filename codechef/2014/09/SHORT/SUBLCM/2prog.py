"""
http://www.codechef.com/COOK50/problems/SUBLCM
"""
from fractions import gcd

T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	A = map(int,raw_input().split())
	dP = [-1]*N
	for i in xrange(N) :
		for j in xrange(i-1,-1,-1) :
			#print [(x,eval(x)) for x in ['i','j','A[i]','A[j]']]
			if gcd(A[i],A[j])!=1 :
				dP[i] = j
				break
		#print dP
		dP[i] = i-dP[i]
		if i > 0 :
			dP[i] = min(dP[i-1]+1,dP[i])
	#print dP
	ans = max(dP)
	if ans == 1 :	print -1
	else :	print ans

