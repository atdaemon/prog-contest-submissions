"""
www.codechef.com/SEPT14/problems/CHEFLR
"""
MOD=10**9+7
T = int(raw_input())
 
for _ in xrange(T) :
	S = str(raw_input())
	curr = 1
	for s in S :
		if s == 'l' :
			if curr%2==0 :
				curr = curr*2 - 1
			else :
				curr = curr*2
		else :
			if curr%2==0 :
				curr = curr*2 + 1
			else :
				curr = curr*2 + 2
		curr=curr%MOD
	print curr

