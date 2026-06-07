class Solution:
    def numDecodings(self, s: str) -> int:
        """
        일단은 매우 기본적인 형태의 fibonachi 계열의 방법론이다.
        0X sequence가 특수 sequence여서 이 경우에만 어떻게 제어를 하면 될거 같다.

        (1112)
        (1) (11, 1)
        자기 자신의 sequence와 바로 앞의 sequence만 보고 싶다.
        (1012)
        (1) dp[0] = 1 if not zero
        (10) dp[1] = dp[0] + current_availe()->(0이니까 불가능, 하지만 10, 1-1) = 1
        dp[2] = dp[1] + current_availe()-> (1-1) = 1
        dp[3] = dp[2] + current_availe()-> (2-1) = 2

        (01)불가, 앞에 0이 있으면 그 sequence는 항상 0 불가능

        robber style이다.
        자신으로부터 앞선 2개의 sub_str과 지금의 자기 자신의 상태만 봐야 한다.

        dp의 정의를 제대로 내리지 못해서 그럼
        [0, i]까지 만들 수 있는 sequence의 수가 되어야함.
        이떄, 1자릿수를 기준으로 한다면 dp[i-1] + (자기자신의 status 변화 + 1)
        그리고, 2자릿수를 기준으로 한다면 dp[i-2] + (자기자신의 status 변화 + 1)

        """
        char_list = list(s)
        # 이런 부분 생각하는 cost가 커서 그렇다.
        one_digit = set([f"{i}" for i in range(1, 10)])
        two_digit = set([f"{i}" for i in range(10, 27)])

        if char_list[0] == "0":
            return 0

        if len(char_list) <= 1:
            return 1 if char_list[0] in one_digit else 0


        dp_table = [0] * len(s)
        dp_table[0] = 1
        dp_table[1] += 1 if "".join(char_list[:2]) in two_digit else 0
        dp_table[1] += 1 if char_list[1] in one_digit else 0


        # def get_val(char_front, char_back):
        #     num = 0
        #     if char_back[-1] in available_char:
        #         num += 1
        #
        #     if char_front+char_back in available_char:
        #         num += 1
        #
        #     return num-1

        # 왜
        for i in range(2, len(s)):
            dp_table[i] += dp_table[i-1] if char_list[i] in one_digit else 0
            dp_table[i] += dp_table[i-2] if "".join(char_list[i-1:i+1]) in two_digit else 0


        return dp_table[-1]