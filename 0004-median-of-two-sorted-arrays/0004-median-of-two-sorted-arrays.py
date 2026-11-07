class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res=sorted(nums1+nums2)
        i=len(res)//2
        if len(res)%2!=0:
            return float(res[i])
        else:
            
            return float((res[i-1]+res[i])/2)
        
        