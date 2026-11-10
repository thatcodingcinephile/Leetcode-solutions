class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join([i[0] for i in words])==s