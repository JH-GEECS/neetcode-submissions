class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        문제를 잘못 이해 했다. 양 옆에서 조여 오는 구조로서 해야 된다.


        :param numbers:
        :param target:
        :return:
        """

        left_idx = 0
        right_idx = len(numbers)-1

        while left_idx < right_idx:
            summation = numbers[left_idx] + numbers[right_idx]
            if summation == target:
                return [left_idx+1, right_idx+1]
            elif summation > target:
                right_idx -= 1
            else:
                left_idx += 1