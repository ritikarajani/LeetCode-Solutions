class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        l = 2
        
        for r in range(2, len(nums)):
            if nums[r] != nums [l-2]:
                nums[l] = nums[r]
                l += 1
        return l
    