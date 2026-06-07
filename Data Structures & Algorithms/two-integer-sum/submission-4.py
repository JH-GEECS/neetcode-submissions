class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        num_dict = defaultdict(int)

        for idx, num in enumerate(nums):
            if (target - num) in num_dict:
                return sorted([idx, num_dict[target - num]])
            else:
                num_dict[num] = idx

        return []