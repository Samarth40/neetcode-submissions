class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for brackets in s:
            if brackets == '(' or brackets == '[' or brackets == '{':
                stack.append(brackets)
            else:
                if brackets == ')' or brackets == ']' or brackets == '}':
                    if len(stack) == 0:
                        return false
                    else:
                        ch = stack.pop()
                if (ch == '(' and brackets == ')') or (ch == '[' and brackets == ']') or (ch == '{' and brackets == '}'):
                    continue
                else:
                    return False
        return len(stack) == 0
                