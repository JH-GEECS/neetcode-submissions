class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        최대 k의 중복을 허용할 수 있음.
        window가 최대 k개의 중복 sequence를 가지는 unique sequnce로
        구성이 되어야 함.
        따라서, 별도로 중복에 대한 counting을 하면서 이것을 기준으로
        window를 collapse를 해야함.
        """

        max_len = 0
        freq_len = 0

        from collections import defaultdict
        char_dict = defaultdict(int)

        left_idx = 0
        for right_idx in range(len(s)):
            char_dict[s[right_idx]] += 1
            
            if char_dict[s[right_idx]] > freq_len:
                freq_len = char_dict[s[right_idx]]

            # 여기 조건만 개선 하면 될 듯 하다.
            while (right_idx - left_idx + 1 - freq_len) > k:
                if char_dict[s[left_idx]] == 1:
                    del char_dict[s[left_idx]]
                else:
                    char_dict[s[left_idx]] -= 1
                left_idx += 1

            max_len = max(max_len, right_idx - left_idx + 1)

        return max_len


        