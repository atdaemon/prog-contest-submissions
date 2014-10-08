"""
http://www.codechef.com/OCT14/problems/CHEFGR
"""
T = int(raw_input())
for _ in xrange(T) :
	N,M = map(int,raw_input().split())
	A = map(int,raw_input().split())
	maxA = max(A)
	need = sum([maxA-i for i in A])
	if (M == need) or (M > need and (M-need)%N==0) :
		print "Yes"
	else :
		print "No"

