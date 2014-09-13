"""
https://www.hackerrank.com/contests/csindia/challenges/roys-rectangle
"""
T = int(raw_input())
for _ in xrange(T) :
	x,y,x1,y1,x2,y2=map(int,raw_input().split())
	print min(x2-x,y2-y,x-x1,y-y1)


