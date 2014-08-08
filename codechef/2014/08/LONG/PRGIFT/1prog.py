"""
http://www.codechef.com/AUG14/problems/PRGIFT
"""
T = int(raw_input())
for _ in xrange(T) :
	N,K = map(int,raw_input().split())
	A = map(int,raw_input().split())
	countEven = len([i for i in A if i%2==0])
	countOdd = N - countEven
	if K == 0 :
		if countOdd >= 1 :
			print "YES"
		else :
			print "NO"
	elif countEven >= K :
		print "YES"
	else :
		print "NO"

