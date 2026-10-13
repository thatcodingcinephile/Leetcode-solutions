class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        res=[nums[nums[i]]for i in range(len(nums))]
        return res
