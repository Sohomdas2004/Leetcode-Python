#Leetcode 16. 3Sum Closest
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res=nums[0]+nums[1]+nums[2]
        nums.sort()

        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1

            while(l<r):
                currsum=nums[i]+nums[l]+nums[r]
                if(currsum==target):
                    res=currsum
                    break
                
                if(abs(target-res)>abs(target-currsum)):
                    res=currsum
                elif(currsum<target):
                    l+=1
                else:
                    r-=1

        return res