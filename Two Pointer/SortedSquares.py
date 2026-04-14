#Lleetcode 977. Squares of a Sorted Array

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        index=len(nums)-1
        l=0
        r=len(nums)-1

        while(l<=r):
            num=0
            if(abs(nums[l])>abs(nums[r])):
                num=nums[l]*nums[l]
                l+=1
            else:
                num=nums[r]*nums[r]
                r-=1
            res[index]=num
            index-=1

        return res