class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        rev=int(str(abs(x))[::-1])*sign 
        return rev if -(2**31)<=rev<=((2**31)-1) else 0
        