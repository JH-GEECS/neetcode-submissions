import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.top_k = nums
        while len(self.top_k) > k:
            heapq.heappop(self.top_k)

        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.top_k, val)

        while len(self.top_k) > self.k:
            heapq.heappop(self.top_k)

        return self.top_k[0]

