class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_unique_char = 0
        from collections import defaultdict
        char_dict = defaultdict(int)

        left_idx = 0
        for right_idx in range(len(s)):
            char_dict[s[right_idx]] += 1
            
            while char_dict[s[right_idx]] > 1:
                if char_dict[s[left_idx]] > 1:
                    char_dict[s[left_idx]] -= 1
                else:
                    del char_dict[s[left_idx]]
                left_idx += 1
            
            max_unique_char = max(max_unique_char, len(char_dict))
        
        return max_unique_char

