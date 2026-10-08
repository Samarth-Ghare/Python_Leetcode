class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        r, sam = [], 0

        for c in s:
            if c == ")":
                sam -= 1
            if sam > 0:
                r.append(c) 
            if c == "(":
                sam += 1

        return "".join(r)