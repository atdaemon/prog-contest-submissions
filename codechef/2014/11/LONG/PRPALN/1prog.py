"""
http://www.codechef.com/NOV14/problems/PRPALN
"""
YES = 'YES'
NO = 'NO'

def solve(inpStr) :
	#print "inpStr = " , inpStr
	if inpStr == inpStr[::-1] : return YES
	stack = list()
	stack.append((0,len(inpStr)-1,0))
	try :
		while True :
			start,end,deletes = stack.pop()
			#print [(x,eval(x)) for x in ['start','end','deletes','stack']]
			if start > end and deletes == 1 :
				return YES
			elif inpStr[start] != inpStr[end] and deletes == 0 :
				stack.append((start+1,end,deletes+1))
				stack.append((start,end-1,deletes+1))
			elif inpStr[start] == inpStr[end] :
				stack.append((start+1,end-1,deletes))
	except :	
		pass
	return NO

T = int(raw_input())
for _ in xrange(T) :
	S = str(raw_input())
	print solve(S)

