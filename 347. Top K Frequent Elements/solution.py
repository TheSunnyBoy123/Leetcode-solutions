from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countdict = Counter(nums)
        
        heap = []

        for key, value in countdict.items():
            heappush(heap, (value, key))
            if len(heap) > k:
                heappop(heap)

        return [i[1] for i in heap]