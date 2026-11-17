class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sortedlist=sorted(nums)
        cons=0
        maxval = 1
        count=1
        if len(nums) == 1:
            return 1
        for i in range(len(sortedlist)):
            if i+1 < len(sortedlist):

                if sortedlist[i] +1 == sortedlist[i+1]:
                    count+=1
                    if count > maxval:  
                        maxval=count
                    cons=1
                    
                    continue
                elif sortedlist[i] == sortedlist[i+1]:
                    continue
                else:                    
                    cons=0
                    count=1
            else:
                if count > maxval: 
                    maxval = count 

        
        if not nums:
            return 0
        else:
            return maxval
        
        
                
