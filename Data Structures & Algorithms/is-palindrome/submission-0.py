class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for char in s:
            if char.isalnum():
                res += char
        print(res)
        l = 0
        r = len(res) - 1

        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        
        return True
        