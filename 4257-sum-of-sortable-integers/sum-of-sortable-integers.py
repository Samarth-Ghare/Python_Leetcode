class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        PrefMax = [0] * n
        PrefMax[0] = nums[0]
        for i in range(1, n):
            PrefMax[i] = PrefMax[i - 1] if PrefMax[i - 1] > nums[i] else nums[i]
            
        SuffMin = [0] * n
        SuffMin[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            SuffMin[i] = SuffMin[i + 1] if SuffMin[i + 1] < nums[i] else nums[i]
            
        PrefD = [0] * n
        for i in range(1, n):
            PrefD[i] = PrefD[i - 1] + (1 if nums[i - 1] > nums[i] else 0)
            
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        ans = 0
        for k in divisors:
            m = n // k
            possible = True
            for i in range(m - 1):
                x = (i + 1) * k - 1
                if PrefMax[x] > SuffMin[x + 1]:
                    possible = False
                    break
            if not possible:
                continue
                
            for i in range(m):
                L = i * k
                R = (i + 1) * k - 1
                global_drops = PrefD[R] - PrefD[L]
                boundary_drop = 1 if nums[R] > nums[L] else 0
                if global_drops + boundary_drop > 1:
                    possible = False
                    break
            if possible:
                ans += k
                
        return ans