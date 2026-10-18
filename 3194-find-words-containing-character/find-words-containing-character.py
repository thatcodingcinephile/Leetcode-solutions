class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=[i for i in range(len(words)) if x in words[i]]
        return l