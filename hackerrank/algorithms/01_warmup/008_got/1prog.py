"""
https://www.hackerrank.com/challenges/game-of-thrones
"""
from collections import Counter
S = str(raw_input())
C = Counter(S)
count = 0
for i in C :
	if C[i] %2 != 0 :
		count+=1
if count <=1 :
	print "YES"
else :
	print "NO"

