class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
            j=len(nums)
            i=0
            s=0
            l=[nums[s],]
            while i<j:
                if nums[i]!=nums[s]:
                    s+=1
                    nums[s]=nums[i]
                i+=1
            return s+1