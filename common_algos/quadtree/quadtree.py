"""
Quadtree implementation
"""
from pprint import pprint
#from logger import log

class QuadTree() :
	capacity = 4
	occupied = 0
	xMin,xMax,yMin,yMax = 0,float("inf"),0,float("inf")
	subTree = None

	def __init__(self,xMin,xMax,yMin,yMax) :
		self.xMin = xMin
		self.xMax = xMax
		self.yMin = yMin
		self.yMax = yMax

	#@log
	def insert(self,x,y) :
		if not (self.xMin<x<=self.xMax and self.yMin<y<=self.yMax) :
			#print((x,y)," not within ",(self.xMin,self.xMax,self.yMin,self.yMax))
			return
		if self.occupied == 0 :
			self.subTree = [(x,y)]
		elif self.occupied ==  self.capacity:
			tempArray = self.subTree
			xMid = (self.xMax+self.xMin)/2
			yMid = (self.yMin+self.yMax)/2
			self.subTree = [
				QuadTree(self.xMin,xMid,self.yMin,yMid),
				QuadTree(xMid,self.xMax,self.yMin,yMid),
				QuadTree(self.xMin,xMid,yMid,self.yMax),
				QuadTree(xMid,self.xMax,yMid,self.yMax),
				]
			for xi,yi in tempArray+[(x,y)] :
				for tree in self.subTree :
					tree.insert(xi,yi)
		elif self.occupied > self.capacity :
			for tree in self.subTree : tree.insert(x,y)
		else : #subTree is not full
			self.subTree.append((x,y))
		self.occupied+=1
		#print(self.occupied,[self.xMin,self.xMax,self.yMin,self.yMax],self.subTree)

	def __str__(self) :
		if self.occupied <= self.capacity :
			_str = str(self.subTree)
		else :
			_str = str([tree.__str__() for tree in self.subTree])
		return _str


	def contains(self,x,y) :
		#print((x,y)," being searched in ",(self.xMin,self.xMax,self.yMin,self.yMax))
		if not (self.xMin<x<=self.xMax and self.yMin<y<=self.yMax) :
			#print((x,y)," not found within ",(self.xMin,self.xMax,self.yMin,self.yMax))
			return False
		if not self.subTree :
			#print("subTree is null for " ,(self.xMin,self.xMax,self.yMin,self.yMax) )
			return False
		if self.occupied <= self.capacity :
			for xi,yi in self.subTree :
				if xi==x and yi == y :
					#print((x,y)," found within ",(self.xMin,self.xMax,self.yMin,self.yMax))
					return True
		else :
			for tree in self.subTree :
				if tree.xMin<x<=tree.xMax and tree.yMin<y<=tree.yMax and tree.contains(x,y) : 
					#print((x,y)," found within ",(self.xMin,self.xMax,self.yMin,self.yMax))
					return True
		return False

if __name__ == "__main__" :
	T,xmin,xmax,ymin,ymax = map(int,raw_input().split())
	q = QuadTree(xmin,xmax,ymin,ymax)
	for _ in xrange(T) :
		x,y = map(int,raw_input().split())
		q.insert(x,y)
	T = int(raw_input())
	for _ in xrange(T) :
		x,y = map(int,raw_input().split())
		ans = q.contains(x,y)
		if ans :
			print((x,y)," is present in quadtree.")
		else :
			pass#print((x,y)," is not present in quadtree.")
