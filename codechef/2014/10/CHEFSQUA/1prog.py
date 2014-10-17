"""
http://www.codechef.com/OCT14/problems/CHEFSQUA
"""
from itertools import combinations
#from logger import log

N = int(raw_input())
diction = {}

def addDict(X,Y,D) :
	"""Add point (X,Y) to dictionary"""
	if X not in D :
		D[X] =  set([])
	d = D[X]
	if Y  not in d :
		d.add(Y)
	#print D
	return D

def isInDict(X,Y,D) :
	"""True if point (X,Y) is in dictionary, else False"""
	if X in D :
		if Y in D[X] :
			return True
	return False

#@log
def adjacents(A,B) :
	X1,Y1 = A
	X2,Y2 = B[0]-X1,B[1]-Y1
	X3,Y3 = X2-Y2,X2+Y2
	X4,Y4 = -Y2,X2
	X5,Y5 = 2*X2-X3,2*Y2-Y3
	X6,Y6 = -X4,-Y4
	return [[(X1+X3,Y1+Y3),(X1+X4,Y1+Y4)],[(X1+X5,Y1+Y5),(X1+X6,Y1+Y6)]]

#@log
def diags(A,B) :
	X1,Y1 = A
	X2,Y2 = B[0]-X1,B[1]-Y1
	if (X2+Y2) % 2 == 0 :
		b = (X2+Y2)/2
		a = X2-b
		return [[(X1+a,Y1+b),(X1+b,Y1-a)]]
	return []
#@log
def sqCoOrds(A,B) :
	"""Given two points, return a list of 2-tuples such that each pair of points completes the square for the given two points"""
	A,B = sorted([A,B])
	return diags(A,B)

#@log
def required(A,B) :
	"""Given two points, return how many points are required to make a square that are not given in input"""
	global diction
	poss = sqCoOrds(A,B)
	ans = 2
	for coords in poss :
		tAns = 2
		#print "Co-ord = ",coords
		A = coords[0]
		B = coords[1]
		if isInDict(A[0],A[1],diction) :
			tAns-=1
		if isInDict(B[0],B[1],diction) :
			tAns-=1
		ans = min(ans,tAns)
		if ans == 0 : return ans
	return ans

#@log
def solve(N,diction,points) :
	"""actual solve. This is supposed to be O(N^2)"""
	ans = 4
	for a,b in combinations(points,2) :
		#print a,b
		reqd = required(a,b)
		ans = min(ans,reqd)
		if ans == 0 : 
			return ans
	return ans

points = [0]*N
for _ in xrange(N) :
	X,Y = map(int,raw_input().split())
	points[_] = (X,Y)
	addDict(X,Y,diction)
#print diction
#print points
#print isInDict(0,100,diction)
#print isInDict(-1,-1,diction)
if N == 0 :
	print 4
elif N == 1 :
	print 3
else :
	print solve(N,diction,points)


