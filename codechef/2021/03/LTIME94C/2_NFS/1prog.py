"""
https://www.codechef.com/LTIME94C/problems/NFS
STATUS : ACCEPTED
"""

T = int(input())
for _ in range(T) : 
    U,V,A,S = map(int,input().split())
    #print(U,V,A,S)
    if U**2 - 2 * A * S <= V**2 : 
        print("YES")
    else :
        print("NO")

