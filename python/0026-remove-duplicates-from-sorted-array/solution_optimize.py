from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the array is empty, there are no unique elements.
        if not nums:
            return 0
        
        # i points to the position of the last unique element.
        i = 0
        
        # j scans through the array starting from index 1.
        for j in range(1, len(nums)):
            # When we find a new value (different from nums[i]),
            # we move i forward and copy nums[j] into nums[i].
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # The number of unique elements is i + 1
        return i + 1


if __name__ == "__main__":
    nums = [1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5,5]
    sol = Solution()
    k = sol.removeDuplicates(nums)
    
    print("k =", k)                 # number of unique elements
    print("unique part =", nums[:k])  # first k elements are the unique values