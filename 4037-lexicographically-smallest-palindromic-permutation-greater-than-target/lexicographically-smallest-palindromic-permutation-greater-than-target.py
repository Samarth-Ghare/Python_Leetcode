class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        f=Counter(s);o=[x for x in f if f[x]&1]
        if len(o)>1:return ""
        c=o[0] if o else "";f[c]-=bool(c);h=len(s)//2;f={x:f[x]//2 for x in "abcdefghijklmnopqrstuvwxyz"};t=target[:h]
        r=f.copy()
        for x in t:r[x]-=1
        if min(r.values())>=0 and (p:=t+c+t[::-1])>target:return p
        for i in range(h-1,-1,-1):
            r=f.copy()
            for x in t[:i]:r[x]-=1
            if min(r.values())<0:continue
            for x in "abcdefghijklmnopqrstuvwxyz":
                if x>t[i] and r[x]:r[x]-=1;p=t[:i]+x+''.join(y*r[y] for y in r);return p+c+p[::-1]
        return ""