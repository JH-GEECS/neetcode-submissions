class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        unique char을 counting하는 int와 이것을 추적할 수 있는 dict 자료형이
        필요하다.
        그리고 s를 순회를 해야 하는데 (right idx), left index를 줄일 수 있다면
        이것을 계속 줄여야 한다.

        """
        if len(s) <= 1:
            return len(s)

        from collections import defaultdict
        char_dict = defaultdict(int)
        char_dict[s[0]] += 1
        num_char = 1

        left_idx = 0
        for right_idx in range(1, len(s)):
            char_dict[s[right_idx]] += 1

            # 아니다 여기 잘못 작성했다. 
            if (right_idx - left_idx +1) == len(char_dict):
                num_char = len(char_dict)
            
            # 그와 동들어 여기 logic도 잘못되었을 거 같다.
            # 여기 검사 logic은 current char수가 최대인 이상은 계속 줄이는 방식

            while len(char_dict) >= num_char:
                if char_dict[s[left_idx]] >=2:
                    char_dict[s[left_idx]] -= 1
                else:
                    if len(char_dict) -1 < num_char:
                        break
                    else:
                        del char_dict[s[left_idx]]
                left_idx += 1



        return num_char

