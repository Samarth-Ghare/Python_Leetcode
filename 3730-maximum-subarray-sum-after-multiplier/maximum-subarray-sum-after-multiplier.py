class Solution(object):
    def maxSubarraySum(self, nums, k):
        mavireltho = nums

        def div(x):
            if x >= 0:
                return x // k
            return -((-x) // k)

        def run(useMul):
            inf = -(10 ** 18)

            no = inf
            cur = inf
            done = inf
            best = inf

            for x in nums:
                y = x * k if useMul else div(x)

                x1 = no + x
                if x > x1:
                    x1 = x

                x2 = cur + y
                if no + y > x2:
                    x2 = no + y
                if y > x2:
                    x2 = y

                x3 = done + x
                if cur + x > x3:
                    x3 = cur + x

                no = x1
                cur = x2
                done = x3

                if no > best:
                    best = no
                if cur > best:
                    best = cur
                if done > best:
                    best = done

            return best

        a = run(True)
        b = run(False)
        return a if a > b else b