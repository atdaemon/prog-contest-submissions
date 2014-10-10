"""
http://www.codechef.com/OCT14/problems/PRPOTION
"""
import heapq

T = int(raw_input())
for _ in xrange(T) :
	R,G,B,M = map(int,raw_input().split())
	rMax = max(map(int,raw_input().split()))
	gMax = max(map(int,raw_input().split()))
	bMax = max(map(int,raw_input().split()))
	h = [-1*rMax,-1*gMax,-1*bMax]
	heapq.heapify(h)
	for _i_ in xrange(M) :
		top = -1*heapq.heappop(h)
		#print "top = " , top
		top=top/2
		heapq.heappush(h,-1*top)
	print -1*heapq.heappop(h)


