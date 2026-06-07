import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        SJF scheduling이랑 유사한데 지금 잠시 멘탈이 흔들
        """
        from collections import Counter, deque
        task_dict = Counter(tasks)

        heap = []
        heapq.heapify(heap)
        for key, val in task_dict.items():
            heapq.heappush(heap, (-val, key))  # cool time 까지 count 하기 위함.

        queue = deque()

        clk_counter = 0
        while heap or queue:
            clk_counter += 1
            if heap:
                _val, key = heapq.heappop(heap)
                val = -_val - 1
                if val > 0:
                    queue.append((clk_counter+n, val, key))

            if queue and queue[0][0] == clk_counter:
                _, val, key = queue.popleft()
                heapq.heappush(heap, (-val, key))
        
        return clk_counter




        