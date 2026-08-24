class Solution:
    def stoneGameVIII(self, A: List[int]) -> int:
        return reduce(lambda x, y: max(x, y-x), list(accumulate(A))[:0:-1])