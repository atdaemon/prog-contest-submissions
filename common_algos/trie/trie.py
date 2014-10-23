"""
Trie implementation
author : @atdaemon
"""
from logger import log

class TrieNode() :
	#@log
	def __init__(self,parent,isWord=False,char=' ',depth=0) :
		self.char = char
		self.depth = depth
		self.parent = parent
		self.isWord = isWord
		self.children = None
		
	#@log
	def addChildNode(self,childChar=' ',isWord=False) :
		if self.children == None :
			self.children = {}
		if childChar not in self.children :
			self.children[childChar] = TrieNode(self,isWord,childChar,self.depth+1)
		return self.children[childChar]

	#@log
	def getChildNode(self,childChar) :
		if self.children and childChar in self.children :
			return self.children[childChar]
		else : return None
	
	def __str__(self) :
		return str({'char' : self.char,'depth': self.depth, 'parent':self.parent,'isWord':self.isWord,'children':self.children})

	def __repr__(self) :
		return "TrieNode("+str(self.char)+")"

class Trie() :
	#@log
	def __init__(self) :
		self.root = TrieNode(None,False,' ',0)
		print "Root = ", self.root

	#@log
	def put(self,word) :
		node = self.root
		for char in word :
			childNode = node.getChildNode(char)
			if not childNode :
				childNode = node.addChildNode(char)
			node = childNode
		node.isWord = True
		return node
	
	#@log
	def isPresent(self,word) :
		node = self.root
		for char in word :
			if char in node.children :
				node = node.getChildNode(char)
			else : return False
		if node.isWord == True :
			return True
		return False
	
	def __str__(self) :
		return str({'Trie' : {'root': self.root}})

if __name__ == "__main__" :
	trie = Trie()
	print trie
	trie.put("a")
	trie.put("abc")
	trie.put("abd")
	trie.put("cba")
	assert False == trie.isPresent("b")
	assert True ==  trie.isPresent("abc")
