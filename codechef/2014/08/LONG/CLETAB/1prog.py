"""
http://www.codechef.com/AUG14/problems/CLETAB
"""

T = int(raw_input())
for _ in xrange(T) :
	N,M = map(int,raw_input().split())
	C = map(int,raw_input().split())
	Cset = set(C)
	tableOcc = [-1]*N
	tableOccNext = [-1]*N
	dIndex = {}
	d = {}
	for num in Cset : d[num] = [] ; dIndex[num] = 0
	for index,num in enumerate(C) :
		d[num].append(index)
	for num in d :
		d[num].append(M)
	
	tablesCleaned = 0
	for index,num in enumerate(C) :
		if num in tableOcc : #if customer is aleady occupying table
			#update 
			tableNum = tableOcc.index(num)
			dIndex[num]+=1
			tableOccNext[tableNum] = d[num][dIndex[num]]
		else :
			if -1 in tableOcc :	#Empty table found
				emptyTable = tableOcc.index(-1)
				tableOcc[emptyTable] = num
				dIndex[num]+=1
				tableOccNext[emptyTable] = d[num][dIndex[num]]
				tablesCleaned+=1
			else :
				#No empty table
				cleanTable = tableOccNext.index(max(tableOccNext))
				tablesCleaned+=1
				tableOcc[cleanTable] = num
				dIndex[num]+=1
				tableOccNext[cleanTable] = d[num][dIndex[num]]
#		x=0; print "\n".join([str([x,str(eval(x))]) for x in locals() if x in ['index','num','tablesCleaned','tableOcc','tableOccNext','dIndex[num]','d[num]']])+"\n"
	print tablesCleaned
