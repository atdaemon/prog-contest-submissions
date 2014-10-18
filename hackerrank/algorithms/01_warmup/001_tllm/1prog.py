"""
https://www.hackerrank.com/challenges/the-love-letter-mystery
"""
T = int(raw_input())
for _ in xrange(T) :
	S = str(raw_input())
	l = len(S)
	ans = 0
	for i in xrange(l/2) :
		ans+=abs(ord(S[i]) - ord(S[l-1-i]))
	print ans

