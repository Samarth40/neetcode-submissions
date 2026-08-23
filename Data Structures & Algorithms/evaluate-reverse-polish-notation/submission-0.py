class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                var1 = stack.pop()
                var2 = stack.pop()

                if i == "+":
                    result = var2 + var1
                elif i == "-":
                    result = var2 - var1
                elif i == "*":
                    result = var2 * var1
                elif i == "/":
                    result = int(var2 / var1)

                stack.append(result)

        return stack[0]