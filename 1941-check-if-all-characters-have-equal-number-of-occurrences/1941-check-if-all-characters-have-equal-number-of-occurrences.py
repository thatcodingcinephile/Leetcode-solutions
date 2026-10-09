class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s=list(s)
        s1=set()
        for i in list(set(s)):
            s1.add(s.count(i))
        return len(s1)==1