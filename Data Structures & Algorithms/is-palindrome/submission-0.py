class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(ch.lower() for ch in s if ch.isalnum())

        left_idx = 0
        right_idx = len(cleaned_s)-1

        while left_idx <= right_idx:
            if not (cleaned_s[left_idx] == cleaned_s[right_idx]):
                return False
            left_idx += 1
            right_idx -= 1

        return True
        