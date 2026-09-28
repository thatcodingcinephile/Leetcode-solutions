class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        numsum,c=0,0
        real=x
        while x>0:
            c=x%10
            numsum+=c
            x//=10
        return numsum if real%numsum==0 else -1