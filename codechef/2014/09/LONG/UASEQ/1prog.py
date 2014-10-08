"""
http://www.codechef.com/SEPT14/problems/UASEQ
"""
import heapq
N,K = map(int,raw_input().split())
A = map(int,raw_input().split())

#create dictionary
D = {}
def addToDict(D,a,d) :
	if (a,d) in D :
		D[(a,d)]+=1
	else :
		D[(a,d)] = 1
	return D

def isEnough(N,K,x) :
	return x*2+K>=N

for i in xrange(N-1) :
	d = A[i+1] - A[i]
	a = A[i] - d*i
	D = addToDict(D,a,d)	#consider using Counter instead of dictionary
#print D	
heap = []
heapq.heapify(heap)
for t in D :
	if isEnough(N,K,D[t]) :
		heapq.heappush(heap,t)
#print heap
num = len(heap)
for _ in xrange(num) :
	a,d = heapq.heappop(heap)
	#print a,d
	ans = K >= len([1 for x,y in zip(A,(a+i*d for i in xrange(N))) if x != y])
	if ans :
		print " ".join(map(str,[a+i*d for i in xrange(N)]))
		break


