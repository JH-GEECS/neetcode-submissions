class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left_idx = 0
        right_idx = len(heights) - 1
        
        max_area = 0
        # 구체적인 index가 필요하다면 저장을 해야 한다. 그런데 그럴 필요는 없다.
        while left_idx < right_idx:
            current_area = (right_idx-left_idx) * min(heights[right_idx], heights[left_idx])  # 구체적인 index를 구하는 것이 아니라 도달을 하는 것이 필요함
            
            if current_area >= max_area:
                max_area = current_area

            if heights[right_idx] >= heights[left_idx]:  # 오른 쪽이 높은 경우
                left_idx += 1
            else:
                right_idx -= 1
        
        return max_area
        