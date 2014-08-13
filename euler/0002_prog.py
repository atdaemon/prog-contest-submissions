"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler002
https://projecteuler.net/problem=2
"""
from itertools import islice

A=B=1
size = 0
N = [0]*100
while A <= 4*10**16 :
	N[size] = A
	size+=1
	A,B = B,A+B
#print N[:size]

T = int(raw_input())
for _ in xrange(T) :
	num = int(raw_input())
	total = 0
	print sum([i for i in N[:size] if i%2==0 and i < num])



