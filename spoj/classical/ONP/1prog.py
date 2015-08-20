"""
http://www.spoj.com/problems/ONP/
"""
import string
#from logger import log

LEFT = 0
RIGHT = 2
VALUE = 1
operators = ['+','-','*','/','^']

#@log 
def RPN(root) :
	return RPN(root[LEFT])+RPN(root[RIGHT])+root[VALUE] if root else ''

#@log
def __solve__(exp,index) :
	"""return (new_index,tree_segment)"""
	root = [None,None,None]
	if exp[index] == '(' :
		index,root[LEFT] = __solve__(exp,index+1)
		root[VALUE] = exp[index]
		index,root[RIGHT] = __solve__(exp,index+1)
		return index+1,root
	elif exp[index] in string.ascii_lowercase :
		root[VALUE] = exp[index]
		index+=1
	return index,root
#@log
def solve(exp) :
	L = len(exp)
	index,root = __solve__(exp,0)
	#print index,root
	print RPN(root)
	
	

T = int(raw_input())
for _ in xrange(T) :
	exp = str(raw_input().strip())
	#print exp
	solve(exp)
