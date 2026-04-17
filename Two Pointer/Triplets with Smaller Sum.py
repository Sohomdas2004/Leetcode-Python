class Solution:
    def countTriplets(self, sum, arr):
        #code herec
        count=0
        arr.sort()
        
        for i in range(len(arr)):
            left=i+1
            right=len(arr)-1
            
            while(left<right):
                num=arr[i]+arr[left]+arr[right]
                if(num<sum):
                    count += (right - left)
                    left+=1
                    # right-=1
                else:
                    right-=1
                    
        return count
