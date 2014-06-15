import timeit
import numpy.random as nprnd
a = ord('a')

T=20
LEN=50000
def randToChr(randInt) :
	return chr(a+randInt%26)

#t3 = timeit.Timer('nprnd.randint(1000, size=10000)','import numpy.random as nprnd') # v3

#print t1.timeit(10)/10
#print t2.timeit(10)/10
#print t3.timeit(10)/10
#print list(nprnd.randint(26,size=10000))
def randStr() :
	return  ''.join(map(lambda x : chr(a+x),nprnd.randint(26,size=LEN)))

print T
for _ in xrange(T) :
	S = randStr()
	S = S+S[::-1]
	pos = nprnd.randint(len(S)-1)
	random_chr = chr(a+nprnd.randint(26))
	S = S[:pos]+random_chr+S[pos:]
	print S
