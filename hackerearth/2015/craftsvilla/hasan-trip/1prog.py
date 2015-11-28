from math import sqrt
N = int(raw_input())
X = [0]*(N+1)
Y = [0]*(N+1)
F = [0]*(N+1)
for i in xrange(1,N+1) :
	X[i],Y[i],F[i] = map(int,raw_input().split())
#print "X",X
#print "Y",Y
#print "F",F
ans = [F[N]]*(N+1)
ans[N] = F[N]
#print "ans",ans
for x in xrange(N-1,0,-1) :
	#print "x",x
	max_x = max([ans[y]-(sqrt(((abs(X[x]-X[y]))**2)+((abs(Y[x]-Y[y]))**2))) for y in xrange(x+1,N+1)])
	ans[x] = F[x] + max_x
	#print "ans[x]",ans[x],"max_x",max_x
print "%f"%(ans[1] if N > 1 else F[1])

	

