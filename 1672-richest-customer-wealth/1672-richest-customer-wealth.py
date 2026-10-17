class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximum=[]
        for i in accounts:
            maximum.append(sum(i))
        return max(maximum)
        