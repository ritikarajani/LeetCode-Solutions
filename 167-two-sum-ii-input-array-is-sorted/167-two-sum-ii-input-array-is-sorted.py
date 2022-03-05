class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexmap = {}
        
        for i in range(len(numbers)):
            if target - numbers[i] in indexmap:
                return [indexmap[target - numbers[i] ]+1, i + 1]
            indexmap[numbers[i]] = i