# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            str_x = str(x)
            return str_x == str_x[::-1]

print(Solution().is_palindrome(10))