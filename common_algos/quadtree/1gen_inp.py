"""
Quadtree sample problem.
Large input generator
Usage :
python2.7 1gen_inp.py <integer>
e.g. python2.7 1gen_inp.py 1000
"""
from random import Random
import sys
if len(sys.argv) < 2 :
	print("Missing argument for limit")
	sys.exit(1)
T = sys.argv[1]
try :
	T = int(T)
except :
	print("Argument should be int")
	sys.exit(1)

XMIN,XMAX = 0,T
YMIN,YMAX = 0,T
#print for inserts
print T,XMIN,XMAX,YMIN,YMAX
r = Random()
s = set()
for i in xrange(T) :
	while True :
		x = r.randint(XMIN,XMAX)
		y = r.randint(YMIN,YMAX)
		if (x,y) not in s :
			s.add((x,y))
			break
#xyList = r.sample([(x,y) for x in xrange(XMIN,XMAX) for y in xrange(YMIN,YMAX)],T)
for x,y in s:
	print x,y
#print for queries
print T
s = set()
for i in xrange(T) :
	while True :
		x = r.randint(XMIN,XMAX)
		y = r.randint(YMIN,YMAX)
		if (x,y) not in s :
			s.add((x,y))
			break

for x,y in s:
	print x,y
