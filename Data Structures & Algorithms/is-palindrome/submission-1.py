class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = [ch.lower() for ch in s if ch.isalnum()]
        lo, hi  = 0, len(cleaned_s)- 1
        while lo <= hi:
            if (cleaned_s[lo] !=  cleaned_s[hi]):
                return False
            else:
                lo += 1
                hi -= 1

        return True
        