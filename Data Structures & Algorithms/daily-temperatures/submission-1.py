class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        from collections import deque
        # stack = list()  # [[idx, temp]]
        stack = deque()  # [[idx, temp]]
        day_list = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack:
                _prev_idx, _prev_temp = stack[-1]
                if _prev_temp < temp:
                    stack.pop()
                    day_list[_prev_idx] = idx - _prev_idx
                else:
                    break
            
            stack.append([idx, temp])

        return day_list