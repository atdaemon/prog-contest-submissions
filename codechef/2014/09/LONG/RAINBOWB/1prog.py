"""
http://www.codechef.com/SEPT14/problems/RAINBOWB
"""
from operator import mul
from math import factorial
#from logger import log

N = int(raw_input())
MOD = 10**9+7

#@log
def nC6(N) :	#this is nCr where r is always 6
	return reduce(mul,[N-i for i in range(6)])/factorial(6)
if N < 13 :
	print 0
else :
	places = (N+1)/2
	print nC6(places-1)%MOD



