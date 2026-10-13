class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ini=sorted(nums)[0]
        fin=sorted(nums)[len(nums)-1]
        res=[]
        for i in range(ini,fin+1):
            if i not in nums:
                res.append(i)
        return res