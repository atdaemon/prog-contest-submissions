"""
http://www.codechef.com/NOV14/problems/POWERMUL
#trying simple solution, hoping it does not time out
"""

T = int(raw_input())
for _ in xrange(T) :
	N,M,Q = map(int,raw_input().split())
	for _i_ in xrange(Q) :
		R = int(raw_input())
		arr = [i for i in xrange(N+1)]
		R = max(R,N-R)
		for _i in xrange(R+1) : arr[_i] = 0
		den = [i for i in xrange(N-R+1)]
		#print N,M,Q,R,arr,den
		for d in xrange(N-R,1,-1) :
			#print d
			dmult = (N/d)*d
			while den[d] !=0 :
				if arr[dmult] > 0 :
					#factorize and subtract
					f1,f2 = d,dmult/d
					times = min(den[d],arr[dmult])
					arr[f2]+=times
					arr[dmult]-=times
					den[d]-=times
					#print [(x,eval(x)) for x in ['d','dmult','f1','f2','times']]
				dmult-=d
				#print [(x,eval(x)) for x in ['d','dmult','arr','den']]
		#print arr,den	
		ans = 1
		for i,j in enumerate(arr) :
			if i>0 and j>0 :
				ans=(ans*pow(i,j,M))%M
				#print [(x,eval(x)) for x in ['i','j','ans']]
		print ans

