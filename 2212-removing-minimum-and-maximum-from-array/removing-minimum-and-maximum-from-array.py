class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        minI = nums.index(min(nums))
        maxI = nums.index(max(nums))

        left = min(minI, maxI)
        right = max(minI, maxI)
        front = right + 1
        back = n - left

        frontBack = (left+1) + (n - right)
        return min(front, back, frontBack)