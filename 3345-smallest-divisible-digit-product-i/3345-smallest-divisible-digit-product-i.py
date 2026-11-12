class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(x):
            if x==0: return 1
            else: return (x%10)*prod(x//10)
        if n<=t:
            return t
        for i in range(n,n*2):
            if prod(i)%t==0:
                return i