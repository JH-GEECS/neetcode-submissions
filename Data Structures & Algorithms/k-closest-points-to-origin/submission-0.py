import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def compute_metric(x, y):
            return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
        
        heap = []
        heapq.heapify(heap)

        for idx, pts in enumerate(points):
            if len(heap) < k:
                heapq.heappush(heap, (-compute_metric(pts, [0,0]), idx))
            else:
                heapq.heappushpop(heap, (-compute_metric(pts, [0,0]), idx))

        return [points[idx] for (dist, idx) in heap]