class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_arr = []
        for i in range(len(arr)):
            if len(new_arr) == len(arr):
                    break
            new_arr.append(arr[i])
            if arr[i] == 0:
                if len(new_arr) == len(arr):
                    break
                new_arr.append(0)
        arr[:] = new_arr[:]
