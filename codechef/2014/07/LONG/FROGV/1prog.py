"""
http://www.codechef.com/JULY14/problems/FROGV
#using union-find algo
"""
#from logger import log #my logger
 
#@log
def findRoots(arr,K) :
    """arr = sorted array , K = distance"""
    if not arr or len(arr) < 2 :
        return arr
    roots = list(arr)
    lastRoot = arr[0]
    for i in xrange(1,len(arr)) :
        if arr[i] - arr[i-1] <= K :
            roots[i] = lastRoot
        else :
            lastRoot = roots[i]
    return roots

N,K,P = map(int,raw_input().split())
A = map(int,raw_input().split())
L = sorted(A)
root = findRoots(L,K)
rootDict = dict(zip(L,root))
#print N,K,P,A
#print rootDict
for _ in xrange(P) :
    P1,P2 = map(int,raw_input().split())
    #print P1,P2
    ans1 = rootDict[A[P1-1]]
    ans2 = rootDict[A[P2-1]]
    if ans1 == ans2 :
        print "Yes"
    else :
        print "No"
 

