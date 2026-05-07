from typing import List

class Solution:
    def removeDuplicates(nums: List[int]) -> int:
        k = [nums[0]]
        a = 0
        b = 1

        while b < len(nums):
            if nums[a] == nums[b]:
                b += 1
                a += 1
            elif nums[a] != nums[b]:
                k.append(nums[b])
                b +=1
                a +=1
        return print(k)
    
Solution.removeDuplicates([1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5,5])
