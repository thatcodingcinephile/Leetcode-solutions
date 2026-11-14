class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m=max(candies)
        return [True if (i+extraCandies)>=m else False for i in candies ]