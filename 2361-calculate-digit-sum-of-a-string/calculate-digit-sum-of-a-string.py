class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            runsum,i = 0,1
            new_s = ""
            for ch in s:
                num = int(ch)
                if i > k:
                   new_s += str(runsum)
                   i = 1
                   runsum= 0 
                runsum+=num
                i+=1
            new_s += str(runsum)
            s = new_s
            
        return s 

        