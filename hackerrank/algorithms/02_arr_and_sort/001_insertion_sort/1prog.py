#!/bin/python
def insertionSort(ar):   
    index = len(ar) - 1
    V = ar[index]
    while index > 0 and ar[index-1] > V :
        ar[index] = ar[index-1]
        index-=1
        print " ".join(map(str,ar))
    ar[index] = V
    print " ".join(map(str,ar))
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

