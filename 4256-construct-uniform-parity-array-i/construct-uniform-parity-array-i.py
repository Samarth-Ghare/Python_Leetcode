class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd=0
        even=0

        for num in nums1:
            if num %2==0:
                even+=1
            else:
                odd+=1
        if even == len(nums1) or odd == len(nums1):
            return True

        elif even>=1 and odd>=1:
            return True
        return False