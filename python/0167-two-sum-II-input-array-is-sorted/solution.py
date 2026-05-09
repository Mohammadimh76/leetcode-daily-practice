from typing import List

class Solution:
    def twoSum(numbers: List[int], target: int) -> List[int]:
        
        right = len(numbers) - 1
        left = 0

        while left < right:
            sum_target = numbers[left] + numbers[right]

            if sum_target == target:
                return [left + 1, right + 1]
            elif sum_target < target:
                left += 1
            else:
                right -= 1

print(Solution.twoSum([2,7,11,15], 9))
