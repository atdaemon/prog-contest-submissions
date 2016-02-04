import bisect
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        for x in B :
            bisect.insort(A,x)
        return A

