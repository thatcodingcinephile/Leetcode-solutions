class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen = set()
        dup = []
        for num in nums:
            if num in seen:
                dup.append(num)
            else:
                seen.add(num)
        return dup