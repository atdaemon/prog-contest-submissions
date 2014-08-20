"""
https://projecteuler.net/problem=11
https://www.hackerrank.com/contests/projecteuler/challenges/euler011
"""
#from logger import log #my logger
from operator import __mul__

grid = [map(int,raw_input().split()) for i in xrange(20)]
streamSets = [[(0,0),(0,1),(1,0)], #horz
		[(0,0),(1,0),(0,1)], #vert
		[(0,0),(1,1),(0,1)], #diag down top half
		[(0,0),(1,1),(1,0)], #diag down bottom half
		[(19,0),(-1,1),(-1,0)],	#diag up top half
		[(19,0),(-1,1),(0,1)]]	#diag up bottom half


def gridStream(grid,startPos,nextNumber,nextRow) :
	gridX = len(grid)
	gridY  = len(grid[0])
	rowX = startPos[0]
	rowY = startPos[1]
	stream = []
	while 0 <=rowX < gridX and 0 <= rowY < gridY :
		posX,posY = rowX, rowY
		arr = []
		while 0 <= posX < gridX and 0 <= posY < gridY :
			arr.append(grid[posX][posY])
			posX+=nextNumber[0]
			posY+=nextNumber[1]
		stream.append(arr)
		rowX+=nextRow[0]
		rowY+=nextRow[1]
	return stream

def maxProd4Array(arr) :
	end = len(arr)-3
	return max([0]+[reduce(__mul__,arr[i:i+4]) for i in xrange(0,end)])

def maxProd4Stream(stream) :
	return max([maxProd4Array(i) for i in stream])

print max([maxProd4Stream(gridStream(grid,i[0],i[1],i[2])) for i in streamSets])

