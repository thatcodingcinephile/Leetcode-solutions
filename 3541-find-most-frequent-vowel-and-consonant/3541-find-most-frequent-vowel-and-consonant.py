class Solution:
    def maxFreqSum(self, s: str) -> int:
        s=list(s)
        l,m=list(),list()
        for i in s:
            if i in "aeiou":
                l.append(s.count(i))
            else:
                m.append(s.count(i))
        vow,cons=max(l) if len(l)>0 else 0,max(m) if len(m)>0 else 0
        return vow+cons