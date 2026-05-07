from typing import List

class Solution:
    def sortedSquares(nums: List[int]) -> List[int]:

        n = len(nums)
        result = [0] * n
        right, left = n - 1, 0
        
        for k in range(n - 1, -1, -1):
            square_left = nums[left] * nums[left]
            square_right = nums[right] * nums[right]

            if square_left > square_right:
                result[k] = square_left
                left += 1
            else:
                result[k] = square_right
                right -= 1
        
        return result

print(Solution.sortedSquares([-4,-1,0,3,10]))