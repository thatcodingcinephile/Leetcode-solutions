class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        t=0
        while n>0:
            t+=(n%10)
            n//=10
        return t
        
