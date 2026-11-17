class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first="".join(sorted(s))
        sec="".join(sorted(t))
        if first != sec:
            return False
        return True