class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first={}
        for c in s:
            first[c] = first.get(c,0) +1
        last={}
        for c in t:
            last[c] = last.get(c,0) +1
        return first == last