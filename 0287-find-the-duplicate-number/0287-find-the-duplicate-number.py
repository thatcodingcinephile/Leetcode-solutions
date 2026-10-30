class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        s=set()
        for n in nums:
            if n in s:
                return n
            s.add(n)