class Solution:
    def numDecodings(self, s: str) -> int:

        dp_table = [0] * (len(s)+1)
        dp_table[0] = 1  # 아무것도 decoding 하지 않는 방법 1

        one_digit = set(f"{i}" for i in range(1,10))
        two_digit = set(f"{i}" for i in range(10, 27))

        for i in range(1, (len(s)+1)):
            if s[i-1] in one_digit:
                dp_table[i] += dp_table[i-1]
            if i>=2 and s[i-2:i] in two_digit:
                dp_table[i] += dp_table[i-2]

        return dp_table[-1]