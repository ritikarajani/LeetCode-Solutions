class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted_nums = sorted(list(nums1[0:m] + nums2))
        
        for index,i in enumerate(sorted_nums):
            nums1[index] = i