class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        dp_table 2개가 필요한데 각각이 최대 값과 최소 값을 저장을 해야 한다.
        dp_max 그래서 이것은 양의 최대값을
        dp_min 이것은 음의 최대 값을 저장하도록 해야 한다.
        기초적인 kadane dp formula는 dp[i] = max(dp[i-1]+s[i], s[i])를 통해서
        임의의 위치에서 i번쨰 위치 까지의 합산의 최대값을 얻는 방식의 점화식이다.

        :param nums:
        :return:
        """

        dp_max = [1] * len(nums)
        dp_max[0] = nums[0]
        dp_min = [1] * len(nums)
        dp_min[0] = nums[0]

        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])

        return sorted(dp_max)[-1]
        dp_table = [1] * len(nums)

        dp_table[0] = nums[0]
        
        """
        값이랑 부호를 계속 가지고 있어야 할 거 같은데
        아니다 이 방법이 맞네, 어느 임의의 위치에서 자기까지 했을 떄의
        최대 값을 consecutive하게 저장 하니까
        마지막에 정렬해서 최대값만 빼면 된다.

        아니넹,

        어쩔 수 없는 것이고
        

        """
        for i in range(1, len(nums)):
            dp_table[i] = max(dp_table[i-1] * nums[i], nums[i])\
        
        return max(dp_table)
        
        