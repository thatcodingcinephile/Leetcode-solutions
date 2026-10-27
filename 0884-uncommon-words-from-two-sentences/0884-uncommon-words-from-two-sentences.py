class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        l=list()
        s1=list(s1.split())
        s2=list(s2.split())
        all_words = s1 + s2
        

        for word in all_words:
            if all_words.count(word) == 1:
                l.append(word)

        return list(dict.fromkeys(l))