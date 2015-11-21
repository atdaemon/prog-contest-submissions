"""
https://www.hackerrank.com/contests/zenhacks/challenges/decrypt-1
"""
#from logger import log

a = ord('a')
z = ord('z')

#@log
def encrypt(inp,k) :
	out = ''.join([chr(ord(c)+k) if ord(c)+k <= z else chr(ord(c)+k-26) for c in inp ])
	#print "encrypt ",k,"inp",inp,"out",out
	return out
#@log
def mismatch(str1,str2) :
	ans = sum([1 for index in xrange(len(str1)) if str1[index]!=str2[index]] or [0])
	#print "mismatch",str1,str2,ans
	return ans
		
encrypt("abc",2)
encrypt("xyz",2)
mismatch("pqr","pqr")
mismatch("pqr","pqs")

T = int(raw_input().strip())
for _ in xrange(T):
	P,E = raw_input().strip().split(' ')
	P,E = str(P),str(E)
	#print P,E
	print min([mismatch(E,encrypt(P,diff)) for diff in xrange(26)])

	

	

