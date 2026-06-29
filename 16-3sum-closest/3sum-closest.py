class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            minSum = nums[i] + nums[i + 1] + nums[i + 2]
            if minSum > target:
                if abs(minSum - target) < abs(closestSum - target):
                    closestSum = minSum
                break

            maxSum = nums[i] + nums[-1] + nums[-2]
            if maxSum < target:
                if abs(maxSum - target) < abs(closestSum - target):
                    closestSum = maxSum
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if abs(currentSum - target) < abs(closestSum - target):
                    closestSum = currentSum

                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    return target

        return closestSum       
