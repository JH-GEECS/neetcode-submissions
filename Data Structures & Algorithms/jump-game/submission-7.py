class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reach_idx = 0
        for i in range(len(nums)):
            max_reach_idx = max(max_reach_idx, i+nums[i])

            if i >= max_reach_idx and nums[i] == 0:
                break

        return True if max_reach_idx >= len(nums)-1 else False