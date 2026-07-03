class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res, size = "", []

        for string in strs:
            size.append(len(string))
            res += str(len(string))
            res += ","
        res += "#"
        
        for char in strs:
            res += char
        return res
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        res, size = [], []
        i = 0

        while s[i] != "#":
            curr = ""
            while s[i] != ",":
                curr += s[i]
                i += 1
            size.append(int(curr))
            i += 1
        
        i+=1
        for sz in size:
            res.append(s[i:i + sz])
            i += sz
        
        return res
