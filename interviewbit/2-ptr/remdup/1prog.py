class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        L = len(A)
        pos = L-1
        while pos > 0 :
            if A[pos] == A[pos-1] :
                del A[pos]
            pos-=1
        return len(A)
        

