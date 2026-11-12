class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == "+":
                val1, val2 = stack[-1],stack[-2]
                stack.append(val1+val2)
            elif operation == "D":
                val = stack[-1]
                stack.append(val*2)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
        
        return sum(stack)
