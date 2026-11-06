class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] in s[:i]:
                return s[i]
        return ""