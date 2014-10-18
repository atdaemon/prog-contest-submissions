"""
https://www.hackerrank.com/challenges/gem-stones
"""
N = int(raw_input())
S = [0]*N
for index in xrange(N) :
	S[index] = set(str(raw_input()))
print len(reduce(set.intersection,S))

