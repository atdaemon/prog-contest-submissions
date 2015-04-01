"""
http://www.codechef.com/LTIME22/problems/CHEFANUP
"""
T = int(raw_input())
#print T
for _ in xrange(T) :
	N,K,L = map(int,raw_input().split())
	arr = [0]*N
	L-=1
	for i in xrange(N) :
		arr[N-1-i] = L%K + 1
		L = L/K
		#print N,K,L,arr
	print " ".join(map(str,arr))

