"""
https://www.hackerrank.com/challenges/mark-and-toys
"""
from collections import Counter
import heapq

def max_toys(prices, rupees):
	#Compute and return final answer over here
	answer = 0
	c = Counter(prices)
	prices = list(set(prices))
	heapq.heapify(prices)
	try :
		while True :
			toy = heapq.heappop(prices)
			price = toy * c[toy]
			if price <= rupees :
				rupees = rupees - price
				answer+=c[toy]
			else :
				number = rupees/toy
				price = number*toy
				if number == 0 :
					break
				answer+=number
				rupees-=(number*toy)
	except IndexError :
		pass
	return answer

if __name__ == '__main__':
	n, k = map(int, raw_input().split())
	prices = map(int, raw_input().split())
	print max_toys(prices, k)

