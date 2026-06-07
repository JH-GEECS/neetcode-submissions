class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        value_arr = defaultdict(list)
        for idx, num in enumerate(nums):
            value_arr[num].append(idx)

        used_arr = [False] * len(nums)

        answer = []
        for idx, num in enumerate(nums):
            if not used_arr[idx]:
                if (target - num) in value_arr:
                    used_arr[idx] = True
                    if len(value_arr[target-num]) == 2:
                        target_idx = value_arr[target-num][-1]
                    else:
                        target_idx = value_arr[target-num][0]
                        if used_arr[target_idx]:
                            continue
                    used_arr[target_idx] = True
                    answer.append(idx)
                    answer.append(target_idx)
                    break
        return answer