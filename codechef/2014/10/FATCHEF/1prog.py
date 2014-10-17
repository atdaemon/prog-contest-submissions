"""
http://www.codechef.com/OCT14/problems/FATCHEF
"""
import heapq

T = int(raw_input())
for _ in xrange(T) :
	N,M = map(int,raw_input().split())
	heap = []
	for _i_ in xrange(M) :
		x,y = raw_input().split()
		y = int(y)
		heapq.heappush(heap,(y,x))
	#print heap
	old_place,old_color = heapq.heappop(heap)
	ans = 1
	try:
		while True :
			new_place,new_color = heapq.heappop(heap)
			if new_color != old_color :
				mult = new_place - old_place
				ans = (ans * mult) % (1000000009)
			old_color,old_place = new_color,new_place
	except IndexError :
		pass
	print ans

		
