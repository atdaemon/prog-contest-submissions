"""
https://www.hackerrank.com/contests/infinitum-jul14/challenges/sherlock-and-divisors
"""

# Sieve of Eratosthenes
# David Eppstein, UC Irvine, 28 Feb 2002

from __future__ import generators
from collections import Counter
#from logger import log	#mylogger
import math

def eratosthenes():
        '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
        D = {}  # map composite integers to primes witnessing their compositeness
        q = 2   # first integer to test for primality
        while 1:
                if q not in D:
                        yield q        # not marked composite, must be prime
                        D[q*q] = [q]   # first multiple of q not already marked
                else:
                        for p in D[q]: # move each witness to its next multiple
                                D.setdefault(p+q,[]).append(p)
                        del D[q]       # no longer need D[q], free memory
                q += 1

primes = []
iter = eratosthenes()

#@log
def gen_primes_upto(n) :
        for i in iter :
                primes.append(i)
                if i > n :
                        break
	return primes
#@log
def next_prime() :
	p = iter.next()
	primes.append(p)
	return p

#gen_primes_upto(32000)

#@log
def primeFactors(num) : # num <= 10**9
	factors = [1]*30 # log(10**9,2) < 30
	numOfFactors = 0
	for prime in primes :
		while num%prime == 0 :
			factors[numOfFactors] = prime
			numOfFactors+=1
			num = num/prime
		if num == 1 : break
	if num > 1 :
		factors[numOfFactors] = num 
		numOfFactors+=1
	C = Counter(factors)
	del C[1]
	return C

#@log
def solve(num) :
	P = primeFactors(num)
	if P[2] == 0 :	
		return 0
	else :
		P[2]-=1
		ans = 1
		for i in P :
			ans = ans*(P[i]+1)
	return ans

T = int(raw_input())
inp = [0]*T
for _ in xrange(T) :
	inp[_] = int(raw_input())
gen_primes_upto(int(math.sqrt(max(inp))))
for i in xrange(T) :
	print solve(inp[i])

#	C = primeFactors(N)
#	if C[2] == 0 :	
#		print 0
#	else :
#		C[2]-=1
#		R = sum(C.values())

