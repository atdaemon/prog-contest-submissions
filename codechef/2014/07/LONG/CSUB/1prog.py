"""
http://www.codechef.com/JULY14/problems/CSUB
"""
 
T = int(raw_input())
for _ in xrange(T) :
    N = int(raw_input())
    S = str(raw_input())
    C = S.count('1')
    print C*(C+1)/2
