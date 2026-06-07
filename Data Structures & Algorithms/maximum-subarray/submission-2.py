class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            else:
                dp[idx] = max(nums[idx], dp[idx-1] + nums[idx])
        
        ans = max(dp)
        return ans