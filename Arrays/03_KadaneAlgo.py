class Solution(object):
    def maxSubArray(self, nums):
        
        x=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            x=max(x+nums[i],nums[i])
            max_sum=max(x,max_sum)
        return max_sum

      #Time Complexity O(n)
      #Space Complexity O(1)
