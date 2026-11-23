class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        a=sum(nums)
        ar=0
        for i in nums:
            while i>0:
                ar+=(i%10)
                i//=10
        return abs(a-ar)