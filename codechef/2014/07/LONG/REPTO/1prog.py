"""
http://www.codechef.com/JULY14/problems/RETPO
"""
#from logger import log#my logger
 
dists={(0,0):0,(0,1):1,(0,-1):-1,
	(1,1):2,(-1,1):2,(-1,-1):2,(1,-1):2,
	(1,0):3,(-1,0):3}
 
#@log
def posSideDist(x,y) :
	if (x,y) in dists :
		return dists[x,y]
	elif min(x,y) >= 1 :
		move = min(x,y)
		return move*2 + posSideDist(x-move,y-move)
	elif x == 0 :
		move = y/2
		return move*4 + posSideDist(x,y%2)
	elif y == 0 :
		move = x/2
		return move*4 + posSideDist(x%2,y)
	return 0

#@log
def solve(x=0,y=0) :
	if (x,y) in dists :
		return dists[x,y]
	elif x >= 0 and y >= 0 :
		return posSideDist(x,y)
	elif x>=0 :
		return posSideDist(x,-y)
	else :
		return min( dists[-1,1] + solve(-x-1,y-1) ,
		dists[-1,-1] + solve(-x-1,y+1)
		)
	return 1
 
T = int(raw_input())
for _ in xrange(T) :
	X,Y = map(int,raw_input().split())
	print solve(X,Y)
 

