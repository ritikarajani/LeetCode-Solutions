class Solution:
    def maxProduct(self, nums: List[int]) -> int:  
        #if len(nums) == 0:
           # return 0
        ans=maxp=minp=nums[0]
        for num in nums[1:]:
            maxp,minp=max(maxp*num,minp*num,num),min(maxp*num,minp*num,num)
            ans = max(maxp,ans)
        return ans
        