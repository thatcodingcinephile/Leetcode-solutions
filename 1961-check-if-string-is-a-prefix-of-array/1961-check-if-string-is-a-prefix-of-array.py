class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        st=""
        for i in words:
            st+=i
            if st==s:
                return True
                break
        return False