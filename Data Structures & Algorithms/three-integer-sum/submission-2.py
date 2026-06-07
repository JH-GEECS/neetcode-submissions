class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        종료 조건을 파악을 해야 한다.
        이상한 edge case를 생각하지 말고 two pointer로 풀 수 있는가를 봐야 한다.
        두 수의 합이
        [-4, -1, -1, 0, 1, 2]
        각 left_idx별로 tuple을 생성하기
        그래서 값이 작으면 mid_idx를 키우기, 값이 크면 right_idx를 줄이기
        값이 같을 때 문제임 그냥, 간단하게 오른 쪽을 줄이도록 하기

        """
        left_idx = 0

        unique_comb = set()  # 아무래도 python이라 가능한 방법 이기는 한데
        nums = sorted(nums)
        while left_idx < len(nums) - 2:
            mid_idx = left_idx + 1
            right_idx = len(nums) - 1

            while mid_idx < right_idx:
                hyp = (nums[left_idx], nums[mid_idx], nums[right_idx])
                sum_hyp = sum(hyp)
                if sum_hyp >= 0:
                    if sum_hyp == 0:
                        unique_comb.add(hyp)
                    right_idx -= 1
                else:
                    mid_idx += 1

            left_idx += 1

        return [list(elem) for elem in unique_comb]