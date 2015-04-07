#!/usr/bin/env python
# Sieve of Eratosthenes
# David Eppstein, UC Irvine, 28 Feb 2002

from __future__ import generators

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

def gen_primes_upto_square_root_of(n) :
        for i in iter :
                primes.append(i)
                if i**2 > n :
                        break

def gen_primes_upto(n) :
        for i in iter :
                primes.append(i)
                if i > n :
                        break

def next_prime() :
	p = iter.next()
	primes.append(p)
	return p

#usage
#gen_primes_upto(10**6)
#gen_primes_upto_square_root_of(10**9)
#print primes

N = int(raw_input("Enter a positive number = ") )
gen_primes_upto_square_root_of(N)
factors = []

for p in primes :
	if N%p == 0 :
		factors.append(p)
print factors

