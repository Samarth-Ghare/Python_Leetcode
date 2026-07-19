def booth(s: str) -> str:
    if not s:
        return s
    s2 = s + s
    n = len(s)
    i, j, k = 0, 1, 0
    while i < n and j < n and k < n:
        if s2[i + k] == s2[j + k]:
            k += 1
            continue
        if s2[i + k] > s2[j + k]:
            i = i + k + 1
            if i <= j:
                i = j + 1
        else:
            j = j + k + 1
            if j <= i:
                j = i + 1
        k = 0

    start = min(i, j)
    return s2[start:start + n]

class Solution:
    def minimumGroups(self, words: List[str]) -> int:
        resset = set([])
        for word in words:
            ew = booth(word[::2])
            ow = booth(word[1::2])
            resset.add((ew,ow))
        return len(resset)
            

        