#!/bin/python
"""
https://www.hackerrank.com/challenges/insertionsort2
"""

def insertionSort(ar):
    L = len(ar)
    index = 1
    while index < L :
        pos = index
        V = ar[pos]
        while pos > 0 and V < ar[pos-1] :
            ar[pos] = ar[pos-1]
            pos-=1
        ar[pos] = V
        print " ".join(map(str,ar))
        index+=1
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

