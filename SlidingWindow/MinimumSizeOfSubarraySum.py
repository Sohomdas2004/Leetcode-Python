
from git import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=len(nums)
        num=0
        left=0

        if(target>sum(nums)):
            return 0

        for right in range(len(nums)):
            num+=nums[right]
            

            while(num>=target):
                res=min(res,right-left+1)
                num-=nums[left]
                left+=1
        return res