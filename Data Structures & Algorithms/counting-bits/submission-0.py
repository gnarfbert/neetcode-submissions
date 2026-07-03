class Solution:
    def countBits(self, n: int) -> List[int]:

        res = [0]

        for i in range(1, n + 1):
            bitString = bin(i)
            count = 0
            for char in bitString:
                if char == '1':
                    count += 1
            res.append(count)
        
        return res
        