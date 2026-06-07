class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        You are given an integer array nums where nums[i] represents the amount of money the ith house has.
        The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

        원형 제약의 본질은 **"한 쌍의 원소(arr[0], arr[n-1])가 동시에 뭘 못한다"**는 거예요.
        이 "동시에 X"를 부정하면: NOT (A이고 B) = NOT A 이거나 NOT B

        :param nums:
        :return:
        """
        # 여전히 edge case를 처리를 해야함
        # 1개 짜리와 2개 짜리 인 경우
        # 이때는 3개짜리도 포함이 되어야 함. 원형이라서 하나 고르면 나머지 양 옆에 못 고름
        if len(nums) <= 3:
            return max(nums)

        dp_front = [0] * (len(nums)-1)
        # 처음 집을 포함하는 경우, 그러나 마지막 집은 포함하지 않는 경우
        # 그러면서, dp_front는 해당 집에 도달 했을 때 취득할 수 있는 돈의 최대치를 의미를 하도록
        dp_front[0] = nums[0]
        dp_front[1] = max(dp_front[0], nums[1])
        for i in range(2, len(nums)-1):
            dp_front[i] = max(dp_front[i-1], dp_front[i-2] + nums[i])
            pass

        dp_back = [0] * (len(nums)-1)
        dp_back[0] = nums[1]
        dp_back[1] = max(dp_back[0], nums[2])
        # 처음 집을 포함하지 않는 경우, 그러나 마지막 집은 포함 하는 경우
        for i in range(2, len(nums)-1):
            dp_back[i] = max(dp_back[i-1], dp_back[i-2]+nums[i+1])
        
        answer = max(dp_front[-1], dp_back[-1])
        return answer
        