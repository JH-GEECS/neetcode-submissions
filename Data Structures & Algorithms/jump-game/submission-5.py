class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        아무리 생각해도 BFS search가 빠를 것 같은데
        """
        visited = [False] * len(nums)

        from collections import deque
        
        queue = deque()

        queue.append((0, nums[0]))  # cur_node, available node
        visited[0] = True

        while queue:
            cur_node, available_dist = queue.popleft()

            # 이건 logic에서 그리 중요하지는 않음
            if cur_node == len(nums)-1:
                return True

            for dist in range(1, available_dist+1):
                if cur_node + dist < len(nums):
                    new_available_dist = nums[cur_node+dist]
                    if not visited[cur_node+dist]:
                        queue.append((cur_node+dist, new_available_dist))
                        visited[cur_node+dist] = True

        return visited[-1]
        


