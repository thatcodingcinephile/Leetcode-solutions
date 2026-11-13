class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n=list(map(int,str(n)))
        s=0
        for i in range(len(n)):
            if i%2==0:
                s+=n[i]
            else:
                s-=n[i]
        return s