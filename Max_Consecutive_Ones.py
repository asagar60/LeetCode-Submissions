class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        count_max = 0
        for i in range(len(nums)):
            count = 0 if nums[i] == 0 else count + 1
            if count >= count_max:
                    count_max = count
        return count_max
