class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq_nums = set(nums)

        if len(nums) != len(uniq_nums):
            return True
        else:
            return False