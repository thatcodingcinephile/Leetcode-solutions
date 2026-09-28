class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=list()
        for i in nums1:
            if i in nums2:
                l.append(i)
        l=set(l)
        return list(l)