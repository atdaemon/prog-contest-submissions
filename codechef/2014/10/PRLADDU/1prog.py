"""
http://www.codechef.com/OCT14/problems/PRLADDU
"""

def nextDinoVilla(L) :
	for villa,nos in enumerate(L) :
		if nos < 0 :
			yield (villa,-1*nos)


T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	D = map(int,raw_input().split())
	if N == 1 :
		print 0
		continue
	dino = nextDinoVilla(D)
	ans = 0
	dinoVilla,dinoCount = dino.next()
	for peopleVilla, peopleCount in enumerate(D) :
		if peopleCount < 0 :
			continue
		#print peopleVilla,peopleCount
		#print dinoVilla,dinoCount
		while peopleCount > 0 :
			people = min(peopleCount,dinoCount)
			dist = abs(peopleVilla-dinoVilla)
			ans+=(people*dist)
			#print peopleVilla,peopleCount,dinoVilla,dinoCount,people,dist,ans
			peopleCount-=people
			dinoCount-=people
			#x=0;print [(x,eval(x)) for x in locals() if x in ['peopleVilla','peopleCount','dinoVilla','dinoCount','people','dist','ans']]
			if peopleCount==0 : 
				continue
			if dinoCount == 0 : 
				dinoVilla,dinoCount=dino.next()
	print ans
