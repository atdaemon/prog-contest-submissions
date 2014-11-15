"""
http://www.codechef.com/NOV14/problems/CHEFSEG
"""
from math import log
T = int(raw_input())
for _ in xrange(T) :
	X,K = map(int,raw_input().split())
	if K == 1 :
		print float(X)/2
		continue
	divs = pow(2,int(log(K,2)))
	divSize = float(X)/divs
	divNum = K - divs
	pos = divNum*divSize + divSize/2
	#print [(x,eval(x)) for x in ['X','K','divs','divSize','divNum','pos']]
	print repr(pos)

