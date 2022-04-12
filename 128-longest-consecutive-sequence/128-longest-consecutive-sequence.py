class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        length = 0
        
        for i in nums:
            if i-1 not in n:
                currN = i
                currL = 1
                
                while(currN + 1) in n:
                    currN += 1
                    currL += 1
                length = max(length,currL)
        return length