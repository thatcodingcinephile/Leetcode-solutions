class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s.split())
        res=[i[::-1] for i in s]
        return " ".join(res)