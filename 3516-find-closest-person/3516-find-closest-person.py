class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return 1 if abs(x-z)<abs(y-z) else 2 if abs(x-z)>abs(y-z) else 0