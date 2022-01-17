class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s=set(arr)
        for i in range(100000000000):
            if i not in s:
                if 0==k:
                    return i
                k-=1
        