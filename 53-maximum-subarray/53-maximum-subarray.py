class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(current_sum+num,num)
            max_sum = max(current_sum,max_sum)
        return max_sum