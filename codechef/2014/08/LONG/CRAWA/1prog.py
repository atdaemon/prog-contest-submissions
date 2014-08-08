"""
http://www.codechef.com/AUG14/problems/CRAWA
# naive, inefficient solution 
#just for testing correctness
"""
#from logger import log 
T = int(raw_input())
inp = [0]*T
out = [0]*T
for _ in xrange(T) :
	X,Y = map(int,raw_input().split())
	inp[_] = [X,Y]
X,Y = zip(*inp)
maxX = max(map(abs,X))
maxY = max(map(abs,Y))
#print maxX, maxY
limit = max(maxX,maxY)
#x=0; print [(x,eval(x)) for x in locals() if x in ['limit','maxX','maxY','inp']]

#@log
def findAllPoints(limit) :
	x,y=0,0	
	dirn = {0:[1,0] , 2:[-1,0], 1:[0,1], 3:[0,-1]}
	dirIndex = 0
	steps = 0
	ans = set()
	ans.add((0,0))
	while x**2 + y**2 <= 2*(limit**2) :
		steps+=1
		for index in xrange(steps) :
			x+=dirn[dirIndex][0]
			y+=dirn[dirIndex][1]
			ans.add((x,y))
		dirIndex= (dirIndex+1)%4
#	r=0; print [(r,eval(r)) for r in locals() if r in ['x','y','dirIndex','steps','ans']]
	return ans

ansSet = findAllPoints(limit)

for index in xrange(T) :
	if tuple(inp[index]) in ansSet :
		print "YES"
	else :
		print "NO"


		
