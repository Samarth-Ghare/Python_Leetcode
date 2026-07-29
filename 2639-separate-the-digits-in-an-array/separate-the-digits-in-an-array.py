class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            s = str(n)
            for ch in s:
                result.append(int(ch))
        return result