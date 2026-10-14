class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        l=[]
        for i in nums:
            if nums.count(i)>=2:
                continue
            else:
                l.append(i)
        return sum(l)