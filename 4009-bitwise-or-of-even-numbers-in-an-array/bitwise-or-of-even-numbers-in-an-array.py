class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            if i%2==0:
                x|=i
        return x