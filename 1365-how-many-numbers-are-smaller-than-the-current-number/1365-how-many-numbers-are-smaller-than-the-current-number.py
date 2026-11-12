class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ar=[]
        for i in range(len(nums)):
            cou=0
            for j in range(len(nums)):
                if i!=j and nums[i]>nums[j]:
                    cou+=1
            ar.append(cou)
        return ar