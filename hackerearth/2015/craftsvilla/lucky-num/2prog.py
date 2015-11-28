import string
"""
trivial algo. used to verify faster algo.
"""
mod = 1000000007
T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	ans = 0
	for x in xrange(N+1) :
		binary = bin(x)[2:]
		if binary.count('1') == 2 :
			ans= (ans+x)%mod
	print ans

