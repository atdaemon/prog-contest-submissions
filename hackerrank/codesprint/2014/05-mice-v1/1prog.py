"""
https://www.hackerrank.com/contests/csindia/challenges/mice-v1
"""
T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	M = sorted(map(int,raw_input().split()))
	H = sorted(map(int,raw_input().split()))
	print max([abs(i-j) for i,j in zip(M,H)])

