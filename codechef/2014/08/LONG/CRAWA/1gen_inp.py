#generate largest input with points near origin

T = 10**5
L = 1000

print T

M = [[x,y] for x in xrange(L) for y in xrange(L)]
M = sorted(M, key=lambda (x,y) : x**2 + y**2)

for index in xrange(T) :
	print M[index][0],M[index][1]

