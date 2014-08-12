"""
http://www.codechef.com/AUG14/problems/CRAWA
"""
from operator import __or__

def f(x,y,fy,count,fmin,fmax) :
	if fy(y) :
		if fmin(count) <= x <= fmax(count) :	
			return True
	return False

T = int(raw_input())
for _ in xrange(T) :
	X,Y = map(int,raw_input().split())
	ans = reduce(__or__,
		[f(X,Y,lambda y: y<=0 and y%2==0, abs(Y)/2, lambda x : x*(-2), lambda x : 1+(2*x)),
		f(X,Y,lambda y: y>0 and y%2==0, (Y/2)-1,lambda x : (-2)*(x+1), lambda x: 1+(2*x)),
		f(Y,X,lambda x:x>0 and x%2==1, X/2, lambda y: (-2)*y, lambda y:2*(y+1)),
		f(Y,X,lambda x: x<0 and x%2==0, (-1)*(X/2), lambda y: (-2)*(y), lambda y: 2*(y))
		]
	)
	print "YES" if ans else "NO"
