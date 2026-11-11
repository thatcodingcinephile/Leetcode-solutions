class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        st=""
        rem=list(t if max(len(s),len(t))==len(s) else s)
        for i in (s if max(len(s),len(t))==len(s) else t):
            if i not in rem:
                st+=i
            else:
                rem.remove(i)
        return st


            