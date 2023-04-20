# LC 217 - Contains Duplicate

# Given an integer array, nums, return true if any value appears at least twice in the 
# array, and return false if every element is distinct.

# Example:
# input: nums = [1,2,3,1]
# output: true

# input: nums = [1,2,3,4]
# output: false

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # create a set
        hashset = set()

        # iterate over the nums list and check if it's in the hashset
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


# testing
nums = [1,2,3,2]
nums1 = [1,2,3,4,5]
nums2 = [1,1]
nums3 = []
test = Solution()
print(test.containsDuplicate(nums))
print(test.containsDuplicate(nums1))
print(test.containsDuplicate(nums2))
print(test.containsDuplicate(nums3))