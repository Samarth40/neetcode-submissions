class Solution:
    def isPalindrome(self, s: str) -> bool:
        # a = list(s)
        # b = s[::-1]
        result = ""
        for ch in s:
            if ch.isalnum():
                result = result + ch.lower()
        if result == result[::-1]:
            return True
        else:
            return False
        