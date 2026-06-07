class Solution:
    def isValid(self, s: str) -> bool:
        queue = list()

        for ch in s:
            if queue:
                last_char = queue[-1]

                poped = False
                if last_char == "[" and ch == "]":
                    queue.pop()
                    poped =True

                if last_char == "(" and ch == ")":
                    queue.pop()
                    poped =True
                
                if last_char == "{" and ch == "}":
                    queue.pop()
                    poped =True

                if not poped:
                    queue.append(ch)

            else:
                queue.append(ch)
            
        if queue:
            return False
        else:
            return True

        