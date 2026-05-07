from typing import List

class Solution:
    def removeElement(nums: List[int], val: int) -> int:
        k = []
        for i in range(len(nums)):
            if nums[i] != val:
                k.append(nums[i])
        return print(k, len(k))
    
Solution.removeElement([0,1,2,2,3,0,4,2], 2)