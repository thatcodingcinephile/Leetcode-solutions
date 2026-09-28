class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
       def selfdiv(x):
            l=list()
            temp=x
            while temp>0:
                c=temp%10
                temp//=10
                l.append(True if c!=0 and x%c==0 else False)
            return all(l)
       l=[i for i in range(left, right+1) if selfdiv(i)==True]
       return l