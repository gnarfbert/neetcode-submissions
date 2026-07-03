class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = {}

        for char in s:
            if char not in charCount:
                charCount[char] = 1
            else:
                charCount[char] += 1
        
        for char in t:
            if char not in charCount:
                return False
            else:
                charCount[char] += 1
        
        for count in charCount.values():
            if count % 2 != 0:
                return False
        
        return True
        