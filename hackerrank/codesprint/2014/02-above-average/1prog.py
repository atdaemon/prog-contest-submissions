"""
https://www.hackerrank.com/contests/csindia/challenges/above-average
"""
from itertools import islice,ifilter

T = int(raw_input())
for _ in xrange(T) :
	N = map(int,raw_input().split())
	avg = float(sum(islice(N,1,len(N))))/(len(N)-1)
	print len(list(ifilter(lambda x:x>avg,islice(N,1,len(N)))))
