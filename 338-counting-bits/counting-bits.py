class Solution:
    def countBits(self, n: int) -> List[int]:
        ans, bits = [0,1,1,2], [1,2]
        
        while len(ans) < n+1:
            bits = bits + [1 + v for v in bits]
            ans.extend(bits)
        
        return ans[:n+1]