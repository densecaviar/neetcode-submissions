class Solution:
    def isPalindrome(self, s: str) -> bool:
        new= "".join(char for char in s if char.isalpha() or char.isdigit())
        return new.lower() == new[::-1].lower()
    