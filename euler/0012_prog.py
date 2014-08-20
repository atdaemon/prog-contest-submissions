"""
http://projecteuler.net/problem=12
https://www.hackerrank.com/contests/projecteuler/challenges/euler012

1+2+3+...N = N*(N+1)/2
one of N and N+1 is even.
they are co primes
find factors individually and multiply to get total
"""
#from logger import log
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
factors = {1:set([1])}
iter = eratosthenes()

def gen_primes_upto(n) :
        for i in iter :
                primes.append(i)
		factors[i] = set([1,i])
                if i > n :
                        break

T = int(raw_input())
inArr = [0]*T
for i in xrange(T) :
	inArr[i] = int(raw_input())
limit = max(inArr)

gen_primes_upto(41041)	#limit found experimentally
#print factors
#@log
def findFactors(num) :
	if num in factors : return factors[num]
	for p in primes :
		if num%p == 0 :
			div = num/p
			divFactors = findFactors(div)
			factors[num] = divFactors.union(set([p*i for i in divFactors]))
			return factors[num]
maxDivisors = {}
maxDivs = 0


for N in xrange(1,41041) :	#limit found experimentally
	total = N*(N+1)/2
	if N%2 == 0 :
		num1,num2 = N/2,N+1
	else :
		num1,num2 = N,(N+1)/2
	
	totalFactors = len(findFactors(num1))*len(findFactors(num2))
	if totalFactors > maxDivs :
		maxDivs = totalFactors
		maxDivisors[maxDivs] = total
	#print N, total, totalFactors
	if totalFactors >limit : break

#print maxDivisors #has max 26 key value pairs
#print len(maxDivisors)

for i in inArr :
	key = min([k for k in maxDivisors.keys() if k>i])
	print maxDivisors[key]
