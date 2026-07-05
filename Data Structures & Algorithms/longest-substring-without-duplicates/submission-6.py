class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        l,r = 0,0

        for r in range(0, len(s)):
            if s[r] in seen:
                res = max(res, len(s[l:r]))
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
        res = max(res, len(s[l:r + 1]))
        return res
        