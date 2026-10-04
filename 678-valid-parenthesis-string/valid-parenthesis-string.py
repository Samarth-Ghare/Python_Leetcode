class Solution:
    def checkValidString(self, s: str) -> bool:
        Min, Max = 0, 0

        for c in s:
            if c == "(":
                Min, Max = Min+1, Max + 1
            elif c == ")":
                Min, Max = Min - 1, Max -1
            else:
                Min, Max = Min - 1, Max + 1
            if Max < 0:
                return False
            if Min < 0:
                Min = 0
        return Min == 0