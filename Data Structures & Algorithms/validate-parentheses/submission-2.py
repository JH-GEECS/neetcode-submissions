class Solution:
    def isValid(self, s: str) -> bool:

        stack = list()

        for ch in s:
            if ch in ["(", "[", "{"]:
                stack.append(ch)
            else:
                if stack:
                    last_ch = stack[-1]
                    if ch == ")":
                        if last_ch != "(":
                            return False
                        else:
                            stack.pop(-1)
                    elif ch == "]":
                        if last_ch != "[":
                            return False
                        else:
                            stack.pop(-1)
                    else:
                        if last_ch != "{":
                            return False
                        else:
                            stack.pop(-1)
                else:
                    return False
        if stack:
            return False
        else:
            return True
            
        