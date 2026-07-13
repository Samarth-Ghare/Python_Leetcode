class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n = '123456789'
        l = []
        for i in range(0, len(n)):
            for j in range(i + 1, len(n) + 1):
                s=int(n[i:j])
                if s>= low and s<=high:
                    l.append(s)
        l.sort()
        return l