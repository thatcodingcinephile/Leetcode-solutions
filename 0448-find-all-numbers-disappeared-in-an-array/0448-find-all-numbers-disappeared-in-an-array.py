class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        x=set(nums)
        y=set(range(1,len(nums)+1))
        return list(y.difference(x))