class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        e=0
        o=1
        n=len(nums)
        while e<n and o<n:
            if nums[e]%2==0:
                e+=2
            elif nums[o]%2==1:
                o+=2
            else:
                nums[e],nums[o]=nums[o],nums[e]
                e+=2
                o+=2
        return nums