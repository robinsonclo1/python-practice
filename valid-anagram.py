class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for char in s:
            if char in letters.keys():
                letters[char] += 1
            else:
                letters[char] = 1
        for char in t:
            if char in letters.keys(): 
                letters[char] -= 1 
            else:
                return False
        for value in letters.values():
            if value != 0:
                return False
        return True

# ChatGPT Advice
# Remove .key(), it's redundant
# Simplify conditionals
# Invert the order of some checks
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False  # Early return if lengths differ

        # letters = {}
        # for char in s:
        #     letters[char] = letters.get(char, 0) + 1
        # for char in t:
        #     if char not in letters:  # If char not in s, return False
        #         return False
        #     letters[char] -= 1
        #     if letters[char] < 0:  # More occurrences in t than in s
        #         return False

        # return all(value == 0 for value in letters.values())



# Alternate Strategy using Counter
# from collections import Counter

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)

