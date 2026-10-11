class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        def sumofdigits(x):
            if x==0: return 0
            else: return (x%10)+sumofdigits(x//10)
        return sumofdigits(x) if x%sumofdigits(x)==0 else -1