class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        a, b = 0,0
        for i in range(32, -1, -1):
            a = a | 1<<i
            hash = set([n & a for n in nums ])
            
            temp = b | 1 << i
            for f in hash:
                if f^temp in hash:
                    b = temp
        return b