"""
https://www.codechef.com/LTIME94C/problems/DATE1
STATUS : ACCEPTED
"""

T = int(input())
for _ in range(T) :
    A,Y,X = map(int,input().split())
    if A >= Y : 
        print(X*Y)
    else : 
        print(X*A+1)

