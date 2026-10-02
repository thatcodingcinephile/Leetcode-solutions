class Solution:
    def reverseDegree(self, s: str) -> int:
        num=list(reversed(range(1,27)))
        alpha=[chr(i) for i in range(97,123)]
        total=0
        for index,ch in enumerate(s,start=1):
            total+=(num[alpha.index(ch)])*index
        return total
