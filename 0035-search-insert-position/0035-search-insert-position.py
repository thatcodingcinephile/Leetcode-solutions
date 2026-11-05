class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums or target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target in nums:
            return nums.index(target)
        for i in range(len(nums) - 1):
            if nums[i] < target < nums[i+1]:
                return i + 1       
        return len(nums)