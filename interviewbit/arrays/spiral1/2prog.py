class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, A):
		m = len(A)  #rows
		n = len(A[0])   #columns
		TL,TR,BR,BL = [0,0],[0,n-1],[m-1,n-1],[m-1,0]
		#print "m",m,"n",n
		#print "TL,TR,BR,BL",TL,TR,BR,BL
		result = []
		up,down,left,right = True,True,True,True
		while up and down and left and right :
			right = up and TL[1] <= TR[1] and TL[0] <= BL[0]
			#print "right",right
			if right :
				x = TL[0]
				for y in xrange(TL[1],TR[1]+1) :
					#print "A[x][y]",A[x][y]
					result.append(A[x][y])

			down = right and TR[0] < BR[0] and TR[1] >= TL[1]
			#print "down",down
			if down :
				y = TR[1]
				for x in xrange(TR[0]+1,BR[0]+1):
					#print "A[x][y]",A[x][y]
					result.append(A[x][y])

			left = down and BR[1] > BL[1] and TL[0] <= BL[0]
			#print "left",left
			if left : 
				x = BR[0]
				for y in xrange(BR[1]-1,BL[1]-1,-1):
					#print "A[x][y]",A[x][y]
					result.append(A[x][y])

			up = left and BL[0] > TL[0] and TR[1] >= TL[1]
			#print "up",up
			if up :
				y = BL[1]
				for x in xrange(BL[0]-1,TL[0],-1) :
					#print "A[x][y]",A[x][y]
					result.append(A[x][y])
			
			TL,TR,BR,BL = [TL[0]+1,TL[1]+1],[TR[0]+1,TR[1]-1],[BR[0]-1,BR[1]-1],[BL[0]-1,BL[1]+1]
			#print "TL,TR,BR,BL",TL,TR,BR,BL
					

		## Actual code to populate result
		return result

s = Solution()

A = [ [1,2],
	  [3,4],
	  [5,6]
	]
print s.spiralOrder(A)

A = [ [1,2,3],
	  [4,5,6],
	  [7,8,9]
	]
print s.spiralOrder(A)

A = [
  [44],
  [36],
  [395],
  [179],
  [249],
  [349],
  [5],
  [139],
]
print s.spiralOrder(A)

A = [[1],[2],[3],[4]]
print s.spiralOrder(A)


A = [
  [75, 371],
  [230, 201],
  [58, 72],
  [128, 166],
  [198, 225],
  [170, 173],
  [401, 77],
  [229, 17],
  [304, 50],
]
print s.spiralOrder(A)

A = [ [1,2,3],[4,5,6] ]
print s.spiralOrder(A)

