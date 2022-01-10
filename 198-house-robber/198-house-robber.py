class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums)):
            a, b = b, max(a+nums[i], b)
        return b
        