import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l1 = [1]*len(nums)
        r1 = [1]*len(nums)
        p1 =1
        p2=1
        for i in range(1,len(nums)):            
            l1[i]=nums[i-1] *p1
            p1 = l1[i]
        
        for i in range(len(nums)-2,-1,-1):
            r1[i] = nums[i+1] * p2
            p2 = r1[i]
                
        ans=[]
        for i in range (len(nums)):
            ans.append(l1[i] * r1[i])
        return ans 

