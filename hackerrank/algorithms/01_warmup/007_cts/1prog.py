"""
https://www.hackerrank.com/challenges/cut-the-sticks
"""
from collections import Counter
import heapq
N = int(raw_input())
A = map(int,raw_input().split())
c = Counter(A)
A = list(set(A))
heapq.heapify(A)

try :
	while True :
		n = heapq.heappop(A)
		print N
		N = N - c[n]
except IndexError :
	pass


