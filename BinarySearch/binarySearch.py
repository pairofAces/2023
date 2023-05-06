# LC 704 - Binary Search

# Given an array of integers, nums, which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def binarySearch(self, nums: list[int], target:int) -> int:
        l, h = 0, len(nums) - 1
        
        while l <= h:
            m = l + ((h - l) // 2) # (l+h) // 2 can potentially cause an overflow in other languages
            
            if nums[m] > target:
                h = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

nums = [-1,0,3,5,9,12] 
target = 9
# Output: 4

test1 = Solution()

print(test1.binarySearch(nums, target))