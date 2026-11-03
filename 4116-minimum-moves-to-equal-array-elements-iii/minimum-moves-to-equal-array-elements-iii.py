class Solution:
    def minMoves(self, fuck: List[int]) -> int:
        return max(fuck) * len(fuck) - sum(fuck)