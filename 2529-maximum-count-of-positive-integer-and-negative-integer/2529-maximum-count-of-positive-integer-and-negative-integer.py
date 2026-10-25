class Solution:
    def maximumCount(self, nums: list[int]) -> int:
            neg,pos=0,0
            for i in nums:
                if i<0:
                    neg+=1 
                elif i>0:
                    pos+=1
                else:
                    pass
            return max(neg,pos)