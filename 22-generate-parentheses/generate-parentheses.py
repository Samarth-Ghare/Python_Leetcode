class Solution:
    def fun(self,open,close,n,tmp,res):
        if open==n and close==n:
            res.append("".join(tmp))
            return
        if open<n:
            tmp.append('(')
            self.fun(open+1,close,n,tmp,res)
            tmp.pop()
        if close<open:
            tmp.append(')')
            self.fun(open,close+1,n,tmp,res)
            tmp.pop()
        return 

    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        tmp=[]
        self.fun(0,0,n,tmp,res)
        return res

        