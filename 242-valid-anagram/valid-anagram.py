class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count, t_count = Counter(s), Counter(t)
        return s_count== t_count