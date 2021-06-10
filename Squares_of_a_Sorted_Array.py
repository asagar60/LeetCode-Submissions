class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squares = sorted([x**2 for x in A])
        return squares
