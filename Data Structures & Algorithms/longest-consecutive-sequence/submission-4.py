class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sortedlist=sorted(nums)
        counts=[]
        cons=0
        count=1
        if len(nums) == 1:
            return 1
        for i in range(len(sortedlist)):
            if i+1 < len(sortedlist):

                if sortedlist[i] +1 == sortedlist[i+1]:
                    count+=1
                    cons=1
                    counts.append(count)
                    continue
                elif sortedlist[i] == sortedlist[i+1]:
                    continue
                else:
                    counts.append(count)
                    cons=0
                    count=1
            else:
                counts.append(count)
        
        if not counts:
            return 0
        else:
            return max(counts)
        
                
