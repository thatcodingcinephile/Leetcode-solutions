class Solution:
    def reverseBits(self, n: int) -> int:
        b=bin(n)[2:].zfill(32)
        rev=b[::-1]
        return int(rev,2)