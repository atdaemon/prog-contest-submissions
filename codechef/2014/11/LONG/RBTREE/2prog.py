"""
http://www.codechef.com/NOV14/problems/RBTREE
# one small optimization
"""
from math import log

Q = int(raw_input())
invert = False

def count(X,Y) :
	#(number,level,color)
	reds,blacks = 0,0
	xLevel = int(log(X,2))
	X = (X,xLevel,xLevel%2)
	yLevel = int(log(Y,2))
	Y = (Y,yLevel,yLevel%2)
	while X[0]!=Y[0] :
		X,Y = (X,Y) if X[0] > Y[0] else (Y,X)
		defColor = X[2]
		#print defColor,X,Y
		X = (X[0]/2,X[1]-1,not X[2])
		if defColor : reds+=1
		else : blacks+=1

	defColor = X[2]
	#print defColor
	if defColor : reds+=1
	else : blacks+=1
	return reds,blacks

for _ in xrange(Q) :
	S = str(raw_input()).split()
	#print S
	case = S[0][1]
	if case == 'i' : #inversion
		#print "inversion"
		invert = not invert
		#print invert
	elif case == 'b' : #count black nodes on path
		#print "black"
		x,y = int(S[1]),int(S[2])
		#print x,y
		red,black = count(x,y)
		print black if not invert else red
	else : #count red nodes on path
		#print "red"
		x,y = int(S[1]),int(S[2])
		#print x,y
		red,black = count(x,y)
		print red if not invert else black

