"""
Longest common subsequence
"""
#from logger import log

#@log
def __longest__(X,Y) :
	"""Given two lists, return all the elements with the longest length"""
	maxLen = max([len(i) for i in X])
	maxLen = max(maxLen,max([len(i) for i in Y]))
	maxList = set([i for i in X if len(i) == maxLen]).union(set([i for i in Y if len(i) == maxLen]))
	return maxList
	
#@log
def LCSrec(X,Y) :
	"""Given two lists X and Y, return the LCS
	This method is recursive implementation.
	Use only for small lists.
	Watch out for max stack depth
	Time complexity O(len(X)*len(Y)) """
	if len(X) == 0 or len(Y) == 0 :
		return [""]
	if X[-1] == Y[-1] :
		return [lcs+X[-1] for lcs in LCSrec(X[:-1],Y[:-1])]
	return __longest__(LCSrec(X,Y[:-1]),LCSrec(X[:-1],Y))
	

#@log
def __append__(X,c) :
	return [i+c for i in X]

#@log
def LCS(X,Y) :
	"""Given two lists X and Y, return the LCS
	This method is non-recursive implementation.
	Time complexity (shhould be) O(len(X)*len(Y)) """
	if len(X) == 0 or len(Y) == 0 :
		return [""]
	#R = C = 0
	xLen = len(X)
	yLen = len(Y)
	row1 = [['']]*(xLen+1)
	row2 = [['']]*(xLen+1)
	i = j = 0
	for i in xrange(yLen) :
		row1 = row2
		row2 = [['']]*(xLen+1)
		#print row1,row2
		for j in xrange(xLen) :
			#print i,j, sum(len(k) for k in row1)
			#print '\n',[(x,eval(x)) for x in ['i','j','X[j]','Y[i]']]
			if X[j] != Y[i] :
				row2[j] = __longest__(row1[j],row2[j-1])
			else :
				row2[j] = __append__(row1[j],Y[i])
			#print [(x,eval(x)) for x in ['i','j','X[j]','Y[i]','row2[j]','row1[j]','row1','row2']]
		#print row2
	return row2[xLen-1]

if __name__ == '__main__' :
	X = str(raw_input().strip())
	Y = str(raw_input().strip())
	print "X = " , X
	print "Y = " , Y
	print "len(X) = ",len(X),"len(Y) = ",len(Y)
	lcs = LCS(X,Y)
	print "LCS(",X,",",Y,") = ",",".join(lcs)
	print "Total = ",len(lcs)

