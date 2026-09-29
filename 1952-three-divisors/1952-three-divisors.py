class Solution:
    def isThree(self, n: int) -> bool:
        f=0
        for i in range(1,n+1):
            if n%i==0:
                f+=1
        return (True if f==3 else False)