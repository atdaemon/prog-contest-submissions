"""
http://www.codechef.com/OCT14/problems/FATCHEF
Assume that the y values are given in sorted order and dont use heap or sort
Also, use faster I/O since the last one timed out
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
	heap = [0]*M
	for _i_ in xrange(M) :
		x,y = inp.next().split()
		y = int(y)
		heap[_i_] = (y,x)
	#print heap
	old_place,old_color = heap[0]
	ans = 1
	_i_ = 1
	try:
		while _i_<= M :
			new_place,new_color = heap[_i_]
			if new_color != old_color :
				mult = new_place - old_place
				ans = (ans * mult) % (1000000009)
			old_color,old_place = new_color,new_place
			_i_+=1
	except IndexError :
		pass
	print ans

		
