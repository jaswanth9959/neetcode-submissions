class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == "+":
                v1,v2 = stack[-1],stack[-2]
                stack.append(v1+v2)
            elif operation == "D":
                val = stack[-1]
                stack.append(2*val)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)
        