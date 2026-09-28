class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def sumofwords(x: List[str]) -> str:
            word=""
            for i in x:
                word+=i
            return word
        return ((sumofwords(word1))==sumofwords(word2))