class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x=n
        prod,total=1,0
        while x>0:
            c=x%10
            prod*=c
            total+=c
            x//=10
        return prod-total