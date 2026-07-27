class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx = 0
        secondmax = 0

        for n in nums:
            if n > maxx:
                secondmax = maxx
                maxx = n
            else:
                secondmax = max(secondmax, n)

        return (maxx-1)*(secondmax - 1)