class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans = 0

        for num in arr1:
            valid, l, r = False, -1, len(arr2)
            while r - l > 1:
                mid = l + (r - l) // 2
                if abs(num - arr2[mid]) <= d:
                    valid = True
                    break
                elif arr2[mid] < num:
                    l = mid
                else:
                    r = mid
            if not valid:
                ans += 1

        return ans