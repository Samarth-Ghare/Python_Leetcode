class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        q1 = num[:half].count('?')
        q2 = num[half:].count('?')
        if (q1 + q2) % 2:
            return True
        s1 = sum(int(x) for x in num[:half] if x != '?')
        s2 = sum(int(x) for x in num[half:] if x != '?')
        return 2 * (s1 - s2) != (q2 - q1) * 9