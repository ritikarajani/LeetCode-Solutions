class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum (nums)
        
        for i in range(len(nums)):
            left += nums[i]
            right -= nums[i]
            
            if left - nums[i] == right:
                return i
        return -1
        
        
        