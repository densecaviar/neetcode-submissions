from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency =defaultdict(int)
        for num in nums:
            frequency[num]+=1
        
        swapped = sorted([(v,k) for k,v in frequency.items()],reverse=True)
        

        i=0;
        ans=[]
        for tup in swapped:
            if i == k:
                return ans
            else:
                ans.append(tup[1])
                i+=1
        return ans
        