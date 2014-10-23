"""
read output of Trie inp generator as input.
Create a trie
"""
from trie import Trie
T = Trie()
N = int(raw_input())
#print N
for _ in xrange(N) :
	S = str(raw_input())
	#print S
	T.put(S)
print T
