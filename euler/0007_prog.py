"""
Project Euler problem #7
https://projecteuler.net/problem=7
https://www.hackerrank.com/contests/projecteuler/challenges/euler007

# Sieve of Eratosthenes
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

def genNPrimes(N) :
	for i in xrange(N) :
		p = iter.next()
		primes.append(p)

T = int(raw_input())
inArr = [0]*T
for _ in xrange(T) :
	inArr[_] = int(raw_input())
limit = max(inArr)

genNPrimes(limit+1)
for i in inArr :
	print primes[i-1]

