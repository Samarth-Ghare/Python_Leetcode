class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in hashM:
                return [i, hashM[difference]]
            else:
                hashM[num] = i