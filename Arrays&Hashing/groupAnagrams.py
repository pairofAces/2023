# LC 49 - Group Anagrams
# Given an array of strings, strs, group the anagrams
# together. You can return the answer in any order.

# An anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.

import collections

# Time Complexity: O(n * m), where (n) is the number of strings in the input, and (m) is the average
#                  length of each string.

# Space Complexity: O(n), where (n) is the number of strings in the input. Because in the worst case,
#                   the 'ans' variable is a defaultdict that stores anagram groups as values. If there are
#                   no anagram groups and each string is unique, each string will be stored seperately. 
#                   Therefore the space complexity depends on the size of the input. 
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        
        return ans.values()

        