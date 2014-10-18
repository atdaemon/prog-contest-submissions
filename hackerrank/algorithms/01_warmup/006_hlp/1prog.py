"""
https://www.hackerrank.com/challenges/halloween-party
"""
T = int(raw_input())
for _ in xrange(T) :
	K = int(raw_input())
	m1 = K/2
	m2 = K - m1
	print m1*m2

