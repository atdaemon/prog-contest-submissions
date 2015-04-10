"""
Segment tree
# this implementation is limited to integer values and min queries
#uses lists of integers to save space, instead of creating objects of type SegmentTree or nodes
#TODO range min query
#TODO store and return the index of min value instead of the value itself
"""
from logger import log

LEFT = 0
RIGHT = 1
VALUE = 2
MIN = 3
MAX = 4
MID = 5
TOTAL = 6

class SegmentTree() :
	@log
        def __init__(self,arr) :
                self.length = len(arr)-1
                self.arr = arr
		self.store = [0]*TOTAL
		self.store[MIN] = 0
		self.store[MAX] = self.length
		#self.store[MID] = (self.store[MIN]+self.store[MAX])/2
                self.build(arr,0,self.length,self.store)
		self.store[VALUE]  = min(self.store[LEFT][VALUE],self.store[RIGHT][VALUE])

	@log
        def build(self,arr,minX,maxX,store) :
		if minX == maxX :
			store[VALUE] = arr[minX]
			store[LEFT] = store[RIGHT] = -1
			store[MIN] = store[MAX] = store[MID] = minX
			return store
			
                mid = (minX+maxX)/2
		store[MID] = mid
		
                #build left subtree
		leftStore = [0]*TOTAL
		store[LEFT] = leftStore
		leftStore[MIN] = minX
		leftStore[MAX] = mid
		self.build(arr,minX,mid,leftStore)
		#leftStore[VALUE] = min(leftStore[LEFT][VALUE],leftStore[RIGHT][VALUE])
                #build right subtree
		rightStore = [0]*TOTAL
		store[RIGHT] = rightStore
		rightStore[MIN] = minX
		rightStore[MAX] = mid
		self.build(arr,mid+1,maxX,rightStore)
		#rightStore[VALUE] = min(rightStore[LEFT][VALUE],rightStore[RIGHT][VALUE])
                #set value for this node
		store[VALUE] = min(store[LEFT][VALUE],store[RIGHT][VALUE])
		return store
		

        def rangeMin(self,minX,maxX) :
                pass#if self.

if __name__ == "__main__" :
	segtree = SegmentTree([2,8,5,77,3,5,9])
	print segtree

