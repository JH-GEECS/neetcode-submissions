class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # number list
        # num_list = [f"{i}" for i in range(10)]
        ops_list = ["+", "-", "*", "/"]


        # runtime stack
        stack = []

        # compute here
        for elem in tokens:
            if elem not in ops_list:
                stack.append(elem)
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                if elem == "+":
                    resultant = int(operand_1) + int(operand_2)
                elif elem == "-":
                    resultant = int(operand_1) - int(operand_2)
                elif elem == "*":
                    resultant = int(operand_1) * int(operand_2)
                elif elem == "/":
                    resultant = int(int(operand_1) / int(operand_2))
                else:
                    raise ValueError()
                stack.append(str(resultant))

        value = int(stack.pop())

        return value