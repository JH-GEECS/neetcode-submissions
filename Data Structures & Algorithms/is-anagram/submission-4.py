class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        s_cnt = Counter(s)
        t_cnt = Counter(t)

        if len(s_cnt) != len(t_cnt):
            return False

        for k,v in s_cnt.items():
            if t_cnt.get(k, 0) != v:
                return False

        return True