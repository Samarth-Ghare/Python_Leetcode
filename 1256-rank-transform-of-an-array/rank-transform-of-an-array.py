from scipy.stats import rankdata
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        return rankdata(arr,'dense').tolist()