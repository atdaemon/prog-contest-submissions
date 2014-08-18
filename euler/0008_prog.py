"""
https://projecteuler.net/problem=8
https://www.hackerrank.com/contests/projecteuler/challenges/euler008
"""
from operator import mul

def split_prod(numStr,K) :
	numList = [int(i) for i in numStr]
	prods = [0]*(len(numList)-K+1)
	prods[0] = reduce(mul,numList[:K])
	for i in xrange(1,len(prods)) :
		prods[i] = prods[i-1]*numList[K+i-1]/numList[i-1]
	return prods

T = int(raw_input())
for _ in xrange(T):
	N,K = map(int,raw_input().split())
	number = str(raw_input())
	splits = [i for i  in number.split('0') if len(i) >=K]
	split_prods = [max(split_prod(i,K)) for i in  splits]+[0]
	print max(split_prods)

