class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        n = len(s)

        prefix_ones = [0] * (n + 1)
        suff_zeros = [0] * (n + 1)

        for i in range(n):
            prefix_ones[i + 1] = prefix_ones[i] + (s[i] == '1')

        for i in range(n - 1, -1, -1):
            suff_zeros[i] = suff_zeros[i + 1] + (s[i] == '0')

        total_ones = prefix_ones[n]
        ans = []

        for t in strs:
            fixed_ones = 0
            questions = 0
            fixed_prefix_ones = 0
            ok = True

            for i in range(n):
                if t[i] == '1':
                    fixed_ones += 1
                    fixed_prefix_ones += 1
                elif t[i] == '?':
                    questions += 1

                if fixed_prefix_ones > prefix_ones[i + 1]:
                    ok = False
                    break

            if not ok:
                ans.append(False)
                continue

            if total_ones < fixed_ones or total_ones > fixed_ones + questions:
                ans.append(False)
                continue

            suff_fixed_zeros = 0

            for i in range(n - 1, -1, -1):
                if t[i] == '0':
                    suff_fixed_zeros += 1

                if suff_fixed_zeros > suff_zeros[i]:
                    ok = False
                    break

            ans.append(ok)

        return ans