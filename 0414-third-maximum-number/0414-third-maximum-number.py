class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        return sorted(list(set(nums)))[-3] if len(set(nums))>=3 else sorted(nums)[-1]