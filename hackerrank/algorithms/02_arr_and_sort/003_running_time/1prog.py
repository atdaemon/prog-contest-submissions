#!/bin/python
"""
https://www.hackerrank.com/challenges/runningtime
"""
def insertionSort(ar):
    L = len(ar)
    index = 1
    count = 0
    while index < L :
        pos = index
        V = ar[pos]
        while pos > 0 and V < ar[pos-1] :
            ar[pos] = ar[pos-1]
            pos-=1
            count+=1
        ar[pos] = V
        index+=1
    return count

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print insertionSort(ar)

