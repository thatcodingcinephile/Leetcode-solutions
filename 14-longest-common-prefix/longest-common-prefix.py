class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs=sorted(strs)
        j=len(strs)
        st=""
        f,l=strs[0],strs[-1]
        for i in range(min(len(f),len(l))):
            if f[i]==l[i]:
                st+=f[i]
            else:
                break
        return st