class MedianFinder:

    def __init__(self):
        self.heap = []
        self.len = 0 
        

    def addNum(self, num: int) -> None:
        self.heap.append(num)
        self.heap.sort()
        self.len += 1

    def findMedian(self) -> float:
        if self.len == 1:
            return self.heap[0]
        
        if self.len % 2 == 0:
            i = 0
            while i < self.len / 2:
                i += 1
            return float((self.heap[i - 1] + self.heap[i]) / 2)
        
        else:
            print(self.heap)
            i = 0
            while i < self.len / 2:
                i += 1
            return float(self.heap[i - 1])
        