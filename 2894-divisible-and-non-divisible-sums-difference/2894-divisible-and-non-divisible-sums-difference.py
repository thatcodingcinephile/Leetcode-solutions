class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k=[i for i in range(1,n+1) if i%m!=0]
        j=[i for i in range(1,n+1) if i%m==0]
        return sum(k)-sum(j)