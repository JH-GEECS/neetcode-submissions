class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        s_cnt = Counter(s)
        t_cnt = Counter(t)

        for k, v in s_cnt.items():
            if k in t_cnt:
                if s_cnt[k] != t_cnt[k]:
                    return False
            else:
                return False
        
        for k, v in t_cnt.items():
            if k in s_cnt:
                if t_cnt[k] != s_cnt[k]:
                    return False
            else:
                return False

        return True