class Solution:
    def canJump(self, nums: List[int]) -> bool:

        reach_idx = 0
        for i in range(len(nums)):
            if i > reach_idx:
                break
            reach_idx = max(reach_idx, i + nums[i])

        return True if reach_idx >= len(nums)-1 else False