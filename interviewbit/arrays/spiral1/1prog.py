class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, A):
		m = len(A)  #rows
		n = len(A[0])   #columns
		print "m",m,"n",n
		result = []
		for index in xrange((m+1)/2) :
			print "index",index
			#right
			print "right"
			i,j = index,index
			print "i,j",i,j
			for k in xrange(i,n-i) :
				print "k",k,"A[i][k]",A[i][k]
				result.append(A[i][k])
			#down
			print "down"
			column,row_start,row_end = n-1-index, index+1, m-1-index
			print "column,row_start,row_end",column,row_start,row_end
			if column >=0:
				for k in xrange(row_start,row_end+1) :
					print "A[k][column]",A[k][column]
					result.append(A[k][column])
			#left
			print "left"
			row, column_start, column_end = row_end, column-1,index
			print "row, column_start, column_end",row, column_start, column_end
			if m>1 :
				for k in xrange(column_start,column_end-1,-1) :
					print "A[row][k]",A[row][k]
					result.append(A[row][k])
			#up
			print "up"
			column,row_start,row_end = column_end,row-1,index+1
			print "column,row_start,row_end",column,row_start,row_end
			if n>1 and column < n-1-index:
				for k in xrange(row_start,row_end-1,-1) :
					print "A[k][column]",A[k][column]
					result.append(A[k][column])
		## Actual code to populate result
		return result

s = Solution()
"""
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
"""

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

