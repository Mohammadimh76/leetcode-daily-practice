from typing import List

class Solution:
    def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

nums = [0,1,0,3,12]
Solution.moveZeroes(nums)
print(nums)  # [1,3,12,0,0] 
