"""
https://www.hackerrank.com/challenges/service-lane
"""
N,T = map(int,raw_input().split())
Arr = map(int,raw_input().split())
for _ in xrange(T) :
	i,j = map(int,raw_input().split())
	print min(Arr[i:j+1])

