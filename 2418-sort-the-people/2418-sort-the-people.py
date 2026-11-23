class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [names[heights.index(i)] for i in sorted(heights,reverse=True)]