class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res=[start+2*i for i in range(n)]
        x=0
        for i in res:
            x^=i
        return x