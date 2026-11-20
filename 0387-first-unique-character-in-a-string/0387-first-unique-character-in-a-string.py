class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.find(s[i],0,i)==-1 and s.find(s[i],i+1)==-1:
                return i
        return -1