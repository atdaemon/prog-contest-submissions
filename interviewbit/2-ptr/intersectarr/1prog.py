class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        L1,L2 = len(A), len(B)
        P1,P2 = 0,0
        ans = []
        while P1 < L1 and P2 < L2 :
            if A[P1] == B[P2] :
                ans.append(A[P1])
                P1,P2=P1+1,P2+1
            elif A[P1] < B[P2] :
                P1+=1
            else :
                P2+=1
        return ans

