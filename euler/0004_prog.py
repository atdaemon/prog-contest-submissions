"""
https://projecteuler.net/problem=4
https://www.hackerrank.com/contests/projecteuler/challenges/euler004
"""
arr = [0]*2470
size = 0
for A in xrange(100,1000) :
	for B in xrange(100,1000) :
		prod = A*B
		strProd = str(prod)
		if strProd == strProd[::-1] :
			arr[size] = prod
			size+=1
			#print A,B,prod
arr.sort()
#print arr
	
T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	print max([i for i in arr if i < N])


