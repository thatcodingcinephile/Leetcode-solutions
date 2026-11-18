class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        elif n==1:
            return True
        else:
            while n%4==0:
                n//=4
            return n==1