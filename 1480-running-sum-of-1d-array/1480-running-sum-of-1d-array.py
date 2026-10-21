class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        tot=0
        res=list()
        for i in nums:
            tot+=i
            res.append(tot)
        return res