class Solution:
    def reverseWords(self, s: str) -> str:
          l=list(s.split())
          return " ".join(l[::-1])