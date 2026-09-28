class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=list(s.split())
        s=l[:k]
        return " ".join(s)