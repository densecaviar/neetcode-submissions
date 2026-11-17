from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists=defaultdict(list)
        l1=[]
        for string in strs:
            key=tuple(sorted(string))
            lists[key].append(string)

        return [values for values in lists.values()]

        
