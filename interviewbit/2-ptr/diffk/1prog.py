class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
		L = len(A)
		if L == 1 : return 0
		p1,p2=0,1
		while p2 < L :
			if A[p2]-A[p1] == B : return 1
			elif A[p2] - A[p1] < B :p2+=1
			else :
				p1+=1
				if p1==p2 : p2+=1
		return 0

S = Solution()
arr,k = [1,3,5],4
out = 1
assert out == S.diffPossible(arr,k)

arr,k = [1,3,4],4
out = 0
assert out == S.diffPossible(arr,k)

