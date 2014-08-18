"""
Euler problem #6
https://www.hackerrank.com/contests/projecteuler/challenges/euler006
https://projecteuler.net/problem=6
"""
T = int(raw_input())
inArr = [0]*T
for _ in xrange(T) :
	inArr[_] = int(raw_input())
outArr = [0]*T
limit = max(inArr)
sumOfSquares = [0]*(limit+1)
for i in xrange(1,limit+1) :
	sumOfSquares[i] = sumOfSquares[i-1]+i**2
squareOfSum = [0]*(limit+1)
for i in xrange(1,limit+1) :
	sums = (i*(i+1))/2
	squareOfSum[i] = sums**2
for i in xrange(T) :
	num = inArr[i]
	print abs(sumOfSquares[num] - squareOfSum[num])
	

