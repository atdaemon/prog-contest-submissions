"""
https://www.codechef.com/submit/IMDB
STATUS : ACCEPTED
"""
T = int(input())
#print(T)
for _ in range(T) :
    N,X = map(int,input().split())
    #print(N,X)
    best = 0
    for _x in range(N) :
        S,R = map(int,input().split())
        #print(S,R)
        if(S <= X and R > best) : 
            best = R
    #print("best",best)
    print(best)

