class Solution:
    def isValid(self, s: str) -> bool:

        match_dict = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = list()

        for ch in s:
            if ch in match_dict:
                if not stack:
                    return False
                else:
                    last_ch = stack.pop(-1)
                    if last_ch != match_dict[ch]:
                        return False
            else:
                stack.append(ch)
            
            # if ch in ["(", "[", "{"]:
            #     stack.append(ch)
            # else:
            #     if stack:
            #         last_ch = stack[-1]
            #         if ch == ")":
            #             if last_ch != "(":
            #                 return False
            #             else:
            #                 stack.pop(-1)
            #         elif ch == "]":
            #             if last_ch != "[":
            #                 return False
            #             else:
            #                 stack.pop(-1)
            #         else:
            #             if last_ch != "{":
            #                 return False
            #             else:
            #                 stack.pop(-1)
            #     else:
            #         return False
        if stack:
            return False
        else:
            return True