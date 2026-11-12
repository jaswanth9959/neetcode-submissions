class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}":"{" , "]":"[", ")":"("}

        stack = []

        for ch in s:
            if ch in closeToOpen and stack:
                close = stack.pop()
                if close != closeToOpen[ch]:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False