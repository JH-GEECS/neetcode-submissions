class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        num_idx_dict = defaultdict(int)
        
        answer = []
        for idx, num in enumerate(nums):
            if (target - num) in num_idx_dict:
                prev_idx = num_idx_dict[target - num]
                answer = [prev_idx, idx]
                return answer
            num_idx_dict[num] = idx                

        return answer