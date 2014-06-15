"""
https://www.hackerrank.com/contests/w4/challenges/palindrome-index
#v1.1
#Fewer comparisions and operations
"""

def isPalindrome(S) :
	return S==S[::-1]

def removeIndex(S,index) :
	#print index
	return S[:index]+S[index+1:]

T = int(raw_input())
#print "T=",T
for _ in xrange(T) :
	S = str(raw_input())
	#print "S=",S
	N = len(S)
	if isPalindrome(S) :
		print -1
		continue
	for index in xrange(N) :
		if S[index] != S[-1*(index+1)] and isPalindrome(removeIndex(S,index)) :
			print index
			break

	
