"""
http://www.codechef.com/AUG14/problems/REVERSE
"""
import sys
from Queue import PriorityQueue

N,M = map(int,raw_input().split())
graphOneWay = {}
graphTwoWay = {}
dFrom1 = [float("inf")]*N

def root(index,arr) :
	root = index
	while  arr[root] != root :
		root = arr[root]
	return root

def dictAdd(dic,name,value) :
	if name not in dic :
		dic[name] = set([value])
	else :
		dic[name].add(value)
	return dic

connComp = range(N)
for _ in xrange(M) :
	X,Y = map(int,raw_input().split())
	X,Y = X-1,Y-1 #0 based DS
	dictAdd(graphOneWay,X,Y)
	dictAdd(graphTwoWay,X,Y)
	dictAdd(graphTwoWay,Y,X)
	small,large = sorted([X,Y])
	connComp[root(large,connComp)] = root(small,connComp)
#	x=0; print "\n".join([str([x,str(eval(x))]) for x in locals() if x in ['X','Y','graphOneWay','graphTwoWay','connComp']])+"\n"

if root(N-1,connComp) != root(0,connComp) :
	# 1 and N are not connected.
	print -1
	sys.exit(0)

#single-source shortest path algo with distance as number of connections that need to be reversed
#Dijkstra's
notVisited = PriorityQueue()
notVisited.put(0)
dFrom1[0] = 0
while notVisited.qsize() > 0 :
	currNode = notVisited.get()
	neighs = graphTwoWay[currNode]
	for neigh in neighs :
		dFromCurrToNeigh = 0 if currNode in graphOneWay and neigh in graphOneWay[currNode] else 1 #counts the number of links to be reversed
		alt = dFrom1[currNode] + dFromCurrToNeigh
		if alt < dFrom1[neigh] :
			dFrom1[neigh] = alt
			notVisited.put(neigh)
#			print "Dist updated d[",neigh,"]=",alt
#		x=0; print "\n".join([str([x,str(eval(x))]) for x in locals() if x in ['currNode','dFrom1[currNode]','neighs','notVisited','alt''neigh']])+"\n"
	
print dFrom1[N-1]

