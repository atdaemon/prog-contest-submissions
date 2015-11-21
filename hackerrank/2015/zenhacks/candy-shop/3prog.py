"""
https://www.hackerrank.com/contests/zenhacks/challenges/candy-shop
"""
denoms = [1,2,5,10,20,50,100]

def changes(amount):
	ways = [0] * (amount + 1)
	ways[0] = 1
	print "ways",ways
	for denom in denoms:
		print "denom",denom
		for j in xrange(denom, amount + 1):
			ways[j] += ways[j - denom]
			print "j",j,"ways",ways
	print "ans",ways[amount]
	return ways[amount]

N = int(raw_input().strip())
print changes(N)

