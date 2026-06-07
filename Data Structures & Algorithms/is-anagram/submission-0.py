class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        s_cnt = Counter(s)
        t_cnt = Counter(t)

        if s_cnt == t_cnt:
            return True
        else:
            return False