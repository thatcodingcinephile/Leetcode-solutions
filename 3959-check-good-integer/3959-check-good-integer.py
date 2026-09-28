class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        def digsum(x: int)-> int:
            c,num=0,0
            while x>0:
                c=x%10
                num+=c
                x//=10
            return num
        def squaresum(x: int)->int:
            c,num=0,0
            while x>0:
                c=x%10
                num+=pow(c,2)
                x//=10
            return num
        return (squaresum(n)-digsum(n)>=50)