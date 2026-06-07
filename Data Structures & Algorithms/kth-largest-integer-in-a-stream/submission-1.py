import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # heapq.heapify(nums)
        # self.top_k = nums
        # while len(self.top_k) > k:
        #     heapq.heappop(self.top_k)
        #
        self.k = k
        self.top_k = heapq.nlargest(k, nums)
        heapq.heapify(self.top_k)


    def add(self, val: int) -> int:
        # heapq.heappush(self.top_k, val)
        #
        # while len(self.top_k) > self.k:
        #     heapq.heappop(self.top_k)
        #
        # return self.top_k[0]
        if len(self.top_k) < self.k:
            heapq.heappush(self.top_k, val)
        else:
            heapq.heappushpop(self.top_k, val)
        
        return self.top_k[0]


