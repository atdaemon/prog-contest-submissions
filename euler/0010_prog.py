"""
Project Euler problem #10
https://projecteuler.net/problem=10
https://www.hackerrank.com/contests/projecteuler/challenges/euler010

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
primes_sum = []
curr_sum = 0
iter = eratosthenes()

def gen_primes_upto(n) :
	global curr_sum
        for i in iter :
                primes.append(i)
		primes_sum.append(curr_sum+i)
		curr_sum+=i
                if i > n :
                        break

def genNPrimes(N) :
	for i in xrange(N) :
		p = iter.next()
		primes.append(p)

def binSearch(Arr,num) :
	start = 0
	end = len(Arr)
	while start <= end :
		pos = (start+end)/2
		if start == end :
			return pos
		elif Arr[pos] < num :
			start=pos+1
		elif Arr[pos] > num :
			end = pos
		elif Arr[pos] == num :
			#x=0;print [(x,eval(x)) for x in locals() if x in ['pos','start','end','Arr','num']]
			return pos


T = int(raw_input())
inArr = [0]*T
for _ in xrange(T) :
	inArr[_] = int(raw_input())
limit = max(inArr)

gen_primes_upto(limit+1)
for i in inArr :
	pos = binSearch(primes,i)
	if primes[pos] != i :
		pos-=1
	print primes_sum[pos]
	
