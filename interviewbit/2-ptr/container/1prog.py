class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        ans = 0
        L = len(A)
        for P1 in xrange(L-1) :
            for P2 in xrange(P1+1,L) :
                ans = max(ans,(P2-P1)*(min(A[P1],A[P2])))
        return ans
        

