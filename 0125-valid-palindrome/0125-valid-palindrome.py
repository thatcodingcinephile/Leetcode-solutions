class Solution:
    def isPalindrome(self, s: str) -> bool:
        fil=''.join(ch.lower() for ch in s if ch.isalnum())
        return fil==fil[::-1]