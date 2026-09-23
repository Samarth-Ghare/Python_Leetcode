class Solution:
    def minOperations(self, nums, x):
        n = len(nums)
        target = sum(nums) - x
        if target == 0:
            return n
        elif target < 0:
            return -1

        res = -1
        currsum = 0
        l = 0
        for r in range(n):
            currsum += nums[r]
            while currsum > target:
                currsum -= nums[l]
                l += 1
            
            if currsum == target:
                res = max(res, (r - l + 1))    
        return n - res if res != -1 else -1