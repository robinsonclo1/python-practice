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
