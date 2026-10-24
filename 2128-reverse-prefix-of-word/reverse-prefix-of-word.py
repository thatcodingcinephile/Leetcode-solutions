class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            return word[:word.index(ch) + 1][::-1] + word[word.index(ch)+ 1:] 
        else:
            return word