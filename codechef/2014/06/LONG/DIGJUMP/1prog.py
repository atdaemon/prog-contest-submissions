"""
http://www.codechef.com/JUNE14/problems/DIGJUMP
"""
import Queue 

def solve() :
	S = str(raw_input())
	N = len(S)
	print N,S
	if N == 1 or S[N-1] == S[0] :
		print 0
		return
	infy = float('inf')
	dist = [infy]*N
	dist[N-1] = 0 
	q = Queue.PriorityQueue()
	q.put(N-1)
	while not q.empty() :
		curr = q.get()
		print "curr: index,value,dist = " , curr, S[curr] , dist[curr]
		print S
		print ' '*(curr)+'^'
		curr_val = int(S[curr])
		range_val_max = min(N-1 , curr+int(S[curr+1])) if curr < N-1 else N-1
		#range_val_min = 0 if curr==0 else max(0,curr-int(S[curr-1]))
		range_val_min = max(0,0 if curr==0 else curr-int(S[curr-1]))
		print "range_val=",range_val_min,range_val_max
		#(int(S[i]) == curr_val) or
		positions = [i for i in xrange(range_val_max) if  (max(0,0 if curr==0 else curr-int(S[curr-1])) < i < N-1 if curr==N-1 else min(N-1,curr+int(S[curr+1])))]

		print "Reachable from ",curr," = ",positions
		if 0 in positions :
			print "Answer = ",dist[curr]+1
			return
		for index in positions :
			if dist[curr]+1 < dist[index] :
				print "Add to Q :",index
				q.put(index)
				dist[index] = dist[curr] + 1
		print "dist = ",dist
				

solve()
