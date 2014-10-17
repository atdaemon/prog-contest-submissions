"""
http://www.codechef.com/OCT14/problems/CHEFPNT
a non-optimal solution
"""

N,M,K = map(int,raw_input().split())
mat = [0]*N
for _ in xrange(N) :
	mat[_] = [0]*M
for _ in xrange(K) :
	i,j = map(int,raw_input().split())
	mat[i-1][j-1] = 1
#print "\n".join(map(str,mat))
P = 0
ans = []
painted = False
for i in xrange(N) :
	for j in xrange(M) :
		if mat[i][j] == 0 and not painted:
			painted = True
			P+=1
			ans.append((i+1,j+1,0))
		elif mat[i][j] == 1 :
			painted = False
	painted = False
print P
print "\n".join([" ".join(map(str,i)) for i in ans])

