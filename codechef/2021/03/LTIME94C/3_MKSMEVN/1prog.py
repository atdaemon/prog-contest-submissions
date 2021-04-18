"""
https://www.codechef.com/LTIME94C/problems/MKSMEVN
STATUS : ACCEPTED
"""

T = int(input())
for _ in range(T) :
    N = int(input())
    A = list(map(int,input().split()))
    if sum(A)%2 == 0 :
        #sum is already even
        print(0)
    elif 0 in A or 2 in A : 
        # by the given formula, only 0 or 2 will transform from even to odd
        print(1)
    else :
        #not possible
        print(-1)

