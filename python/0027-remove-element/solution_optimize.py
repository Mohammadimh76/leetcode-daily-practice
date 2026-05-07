from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # slow
        for i in range(len(nums)):  # fast
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# Time: O(n)
# Space: O(1) 