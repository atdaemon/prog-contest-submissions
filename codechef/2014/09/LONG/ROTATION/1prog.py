"""
http://www.codechef.com/SEPT14/problems/ROTATION
"""
N,M = map(int,raw_input().split())
A = map(int,raw_input().split())
start = 0
for _ in xrange(M) :
	Q = str(raw_input())
	command,pos = Q.split()
	pos = int(pos)
	
	if command == 'C' :
		start = (start+pos)%N
	elif command == 'A' :
		start = (start+N-pos)%N
	else : #command == 'R'
		print A[(start+pos-1)%N]
	
