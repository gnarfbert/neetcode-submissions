class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = collections.defaultdict(int)
        res = []
        hq = []
        for num in nums:
            map[num] += 1
        
        for key,v in map.items():
            heapq.heappush(hq, (-v, key))

        while k > 0:
            res.append(heapq.heappop(hq)[1])
            k -= 1
        print(res)
        return res

        