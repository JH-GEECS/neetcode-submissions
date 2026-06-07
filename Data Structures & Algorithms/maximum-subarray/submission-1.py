class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import math
        dp_table = [-math.inf] * len(nums)

        dp_table[0] = nums[0]
        for i in range(1, len(nums)):
            dp_table[i] = max(dp_table[i-1]+nums[i], nums[i])
        
        # 아오 진짜 바보다.
        return max(dp_table)