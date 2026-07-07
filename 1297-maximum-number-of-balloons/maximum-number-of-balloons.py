class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target="balloon"
        counter=Counter(text)
        ballonCounter=Counter(target)
        res=float("inf")
        for char in target:
            # print("counter[char]//ballonCounter[char]",counter[char]//ballonCounter[char])
            res=min(res,counter[char]//ballonCounter[char])
        return 0 if res==float("inf") else res
        