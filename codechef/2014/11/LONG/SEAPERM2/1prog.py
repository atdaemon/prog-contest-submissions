"""
http://www.codechef.com/NOV14/problems/SEAPERM2
"""
from itertools import permutations as perm
DATA = 0
MISSING = 1
S1 = []
D = {}
def getPossList(arr,index) :
	global S1
	T1 = tuple(arr)
	if index in D and T1 in D[index] : return D[index][T1]
	length = len(arr) 
	arr = [(i+1 if i >= index else i) for i in arr]
	S2 = set(arr)
	fillNum = list(S1.difference(S2))[0]
#	print "S1 = ", S1
#	print "New arr = " , arr
#	print "fillNum = ",fillNum
	ans = set()
	for i in xrange(length+1) :
		genPoss =  arr[:i]+[fillNum]+arr[i:]
		genPoss = tuple(genPoss)
#		print genPoss
		ans.add(genPoss)

	if index not in D : D[index] = {}
	D[index][T1] = ans
#	print "D " , D
	return ans

T = int(raw_input())

for _ in xrange(T) :
	N = int(raw_input())
	mat = [0]*N
	S1 = set(xrange(1,N+1))
#	print "S1 = " , S1
	for _i_ in xrange(N) :
		mat[_i_] = [map(int,raw_input().split()),0]
		mat[_i_][MISSING] = list(S1.difference(set(mat[_i_][0])))[0]
#	print mat
	
	for arr in perm(mat) :
		ans = getPossList(arr[0][0],1)
		for i in xrange(1,N) :
			ans = ans.intersection(getPossList(arr[i][0],i+1))
#			print ans
			if len(ans) == 0 :
				break
		if len(ans) > 0 :
			print " ".join(map(str,list(ans)[0]))
			break

