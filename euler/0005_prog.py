"""a
https://projecteuler.net/problem=5
https://www.hackerrank.com/contests/projecteuler/challenges/euler005
"""
from fractions import gcd

N = 1
S = 1
arr = [0]*41


def lcm(a,b) :
	return (a*b)/gcd(a,b)

for N in xrange(1,41) :
	S = lcm(S,N)
	arr[N] = S
	#print S
#print arr

T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	print arr[N]
	

