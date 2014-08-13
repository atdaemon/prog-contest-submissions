"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler001
https://projecteuler.net/problem=1
"""
T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	ans = 0
	ans3 = (N-1)/3
	ans3 = 3*(ans3*(ans3+1))/2

	ans5 = (N-1)/5
	ans5 = 5*ans5*(ans5+1)/2

	ans15 = (N-1)/15
	ans15 = 15*ans15*(ans15+1)/2

	ans = ans3 + ans5 - ans15

	print ans



