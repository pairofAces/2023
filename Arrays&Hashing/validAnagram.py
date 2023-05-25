# LC 242 - Valid Anagram

# Given two strings, s and t, return true if (t) is an anagram of (s), and false 
# otherwise.

# note: an anagram is a word of phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once

# Example
# input: s = "anagram", t = "nagaram"
# output: true

# input: s = "rat", t = "car"
# output: false


# Time Complexity: O(n), where (n) is the size of the input strings. This is due to the
#                  code containing a loop that iterates over the entire length of the strings.

# Space Complexity: O(n), where (n) is the amount of unique characters in the dictionaries that were created. This
#                   is because the dictionaries (countS) and (countT) are used to store the
#                   character counts of strings (s) and (t). Since we can assume both strings
#                   are of equal length, the number of unique characters in the dicitonaries
#                   is limited to the length of the strings, in the worst case.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check base scenario if the lengths of both strings are different
        if len(s) is not len(t):
            return False
        
        # initialize two dicitonaries for each input string
        countS, countT = {}, {}

        # iterate over the (s) input string
        for i in range(len(s)):
            # increment the occurance of the current character in (s)
            countS[s[i]] = 1 + countS.get(s[i], 0)

            # increment the occurance of the current character in (t)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # Check if the dictionaries storing the character count are equal
        return countS == countT

# Testing
s = "anagram"
t = "nagaram"

s1 = "rat"
t1 = "car"

test = Solution()
print(test.isAnagram(s, t))
print(test.isAnagram(s1, t1))