"""
http://www.codechef.com/OCT14/problems/FATCHEF
trying faster I/O, because the last submission timed out
"""
import heapq
import sys

def getLine() :
	for line in sys.stdin.xreadlines() :
		yield str(line).strip()

inp = getLine()

T = int(inp.next())
for _ in xrange(T) :
	N,M = map(int,inp.next().split())
	heap = []
	for _i_ in xrange(M) :
		x,y = inp.next().split()
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

		
