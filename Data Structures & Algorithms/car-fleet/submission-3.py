from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleets = 0  # 찾고 싶은 해
        max_time = 0  # 이를 위한 greedy solution의 보조 변수

        cars = sorted([(pos, (target-pos)/spd) for pos, spd in zip(position, speed)])

        for pos, req_time in cars[::-1]:
            if req_time > max_time:
                max_time = req_time
                fleets += 1

        return fleets
