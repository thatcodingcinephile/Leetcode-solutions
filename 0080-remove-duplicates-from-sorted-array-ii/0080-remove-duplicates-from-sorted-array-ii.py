class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        else:
            j=len(nums)
            i=2
            s=1
            l=[nums[s],]
            while i<j:
                if nums[i]!=nums[s-1]:
                    s+=1
                    nums[s]=nums[i]
                i+=1
            return s+1