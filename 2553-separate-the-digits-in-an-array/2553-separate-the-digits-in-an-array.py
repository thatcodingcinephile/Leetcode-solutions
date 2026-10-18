class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        def digsep(x):
            l=list()
            c=0
            while x>0:
                c=x%10
                l.append(c)
                x//=10
            return l
        l=[]
        for i in nums:
            l.extend(digsep(i)[::-1])
        return l