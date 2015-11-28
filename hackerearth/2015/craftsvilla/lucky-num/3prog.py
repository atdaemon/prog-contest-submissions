import string
"""
faster than prog1 due to memoization
"""
small_ans = {1:0,2:0,3:3,4:3,5:8,6:14,7:14,8:14,9:23}
memoize = {}
mod = 1000000007
T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	#print "N",N
	if N in small_ans :
		print small_ans[N]
	else :
		binary = bin(N)[2:]
		#print "binary",binary
		ones = string.count(binary,'1')
		#print "ones",ones
		if ones == 1 :
			width = len(binary) - 1
			#print "width",width
			ans = memoize[width] if width in memoize else ((width-1)*((pow(2,width,mod)+mod-1)%mod))%mod
			memoize[width] = ans
			print ans
		else :
			#second one
			one_two = binary.find('1',binary.find('1')+1)#position of second one
			p = len(binary)
			one_two = p - one_two
			#print "one_two",one_two,"p",p
			ans1 = ((pow(2,one_two,mod)+mod-1)%mod + (one_two*(pow(2,p-1,mod))))%mod
			width = len(binary)-1
			ans2 = memoize[width] if width in memoize else ((width-1)*((pow(2,width,mod)+mod-1)%mod))%mod
			memoize[width] = ans2
			#print "ans1",ans1,"ans2",ans2
			ans = (ans1+ans2)%mod
			print ans

