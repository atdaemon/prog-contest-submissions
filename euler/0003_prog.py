"""
https://projecteuler.net/problem=3
https://www.hackerrank.com/contests/projecteuler/challenges/euler003
#Sieve of Eratosthenes by -
# David Eppstein, UC Irvine, 28 Feb 2002
"""
from __future__ import generators
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

def gen_primes_upto(n) :
        for i in iter :
                primes.append(i)
                if i > n :
                        break

def next_prime() :
	p = iter.next()
	primes.append(p)
	return p

T = int(raw_input())
inputArr = [0]*T
outputArr = [1]*T

def maxPrimeFactor(N) :
	maxFactor = 1
	limit = int(math.sqrt(N)) + 1
	index = 0
	global primes

	while N > 1 :
		prime = primes[index]
		if prime > limit : 
			maxFactor = max(maxFactor,N)
			break
		if N%prime == 0 :
			maxFactor = max(maxFactor,prime)
			N = N/prime
			limit = int(math.sqrt(N)) + 1
		else :
			index+=1
#		x=0; print [(x,eval(x)) for x in locals() if x in ['N','prime','limit','maxFactor','index']]
	return maxFactor	

for i in xrange(T) :
	inputArr[i] = int(raw_input())

gen_primes_upto(int(math.sqrt(max(inputArr)))+1)

for i in xrange(T):
	outputArr[i] = maxPrimeFactor(inputArr[i])
print "\n".join(map(str,outputArr))

