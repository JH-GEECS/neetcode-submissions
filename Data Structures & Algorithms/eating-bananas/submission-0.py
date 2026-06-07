class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        import math

        left_rate = 1
        right_rate = 10 ** 9

        answer = right_rate
        while left_rate <= right_rate:
            mid_rate = (left_rate + right_rate) // 2
            run_time_list = [int(math.ceil(pile / mid_rate)) for pile in piles]
            run_time = sum(run_time_list)

            if run_time <= h:
                right_rate = mid_rate - 1
                answer = mid_rate
            else:
                left_rate = mid_rate + 1

        return answer




