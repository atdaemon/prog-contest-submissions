"""
https://www.codechef.com/submit/IMDB
STATUS : ACCEPTED
"""
T = int(input())
#print(T)
for _ in range(T) :
    N,X = map(int,input().split())
    #print(N,X)
    print(max(
        filter(
            lambda x : x[0] <= X, 
            [list(map(int,input().split())) for _x in range(N)]
        ),
        key = lambda y : y[1]
        )[1]
    )

