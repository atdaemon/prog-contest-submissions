"""
http://www.codechef.com/NOV14/problems/RBTREE
"""
from math import log

Q = int(raw_input())
invert = False

def count(X,Y) :
	reds,blacks = 0,0
	while X!=Y :
		X,Y = max(X,Y),min(X,Y)
		defColor = int(log(X,2))%2
		#print defColor,X,Y
		X = X/2
		if defColor : reds+=1
		else : blacks+=1

	defColor = int(log(X,2))%2
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

