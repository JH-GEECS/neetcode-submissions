class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        num_dict = defaultdict(int)

        for elem in nums:
            num_dict[elem] += 1

        import heapq

        heap = list()
        for num, v in num_dict.items():
            heapq.heappush(heap, (-v, num))

        answer_list = []
        for i in range(k):
            _freq, num = heapq.heappop(heap)
            answer_list.append(num)

        return answer_list
         