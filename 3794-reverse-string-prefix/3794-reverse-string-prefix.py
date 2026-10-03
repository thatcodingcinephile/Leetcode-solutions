class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        st=""
        for i in range(0,k):
            st+=s[i]
        return st[::-1]+s[k::1]