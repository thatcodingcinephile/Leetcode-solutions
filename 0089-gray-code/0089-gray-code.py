class Solution:
    def grayCode(self, n: int) -> list[int]:
        return [i^(i>>1) for i in range(2**n)]