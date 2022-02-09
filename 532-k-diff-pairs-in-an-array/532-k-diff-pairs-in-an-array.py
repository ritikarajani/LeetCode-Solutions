class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        if k > 0:
            return sum([i + k in count for i in count])
        else:
            return sum([count[i] > 1 for i in count])
        