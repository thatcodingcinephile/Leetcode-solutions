class Solution:
    def lengthOfLastWord(self, s: str) -> int:
         l=list(s.strip().split())
         length=len(l)
         return len(l[length-1])