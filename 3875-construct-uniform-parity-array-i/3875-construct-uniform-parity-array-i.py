class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return all(list(filter(lambda x: X%2==0,nums1)))