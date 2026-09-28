class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l=list(map(str,nums))
        count=0
        for i in l:
            if len(i)%2==0:
                count+=1
        return count