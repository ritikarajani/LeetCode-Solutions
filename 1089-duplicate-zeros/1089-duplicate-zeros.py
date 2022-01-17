class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        new = []
        for num in arr:
            if num == 0:
                new.append(0)
                new.append(0)
            else:
                new.append(num)
        for num in range(n):
            arr[num] = new[num]
        