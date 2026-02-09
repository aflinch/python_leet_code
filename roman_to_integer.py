#Roman numerals are represented by seven different symbols:
# I, V, X, L, C, D and M.

#For example, 2 is written as II in Roman numeral,
# just two ones added together. 12 is written as XII,
# which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

#Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used: Given a roman numeral,
# convert it to an integer.

class Solution:
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def roman_to_int(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and self.roman_numerals[s[i]] < self.roman_numerals[s[i + 1]]:
                total -= self.roman_numerals[s[i]]
            else:
                total += self.roman_numerals[s[i]]

        return total

print(Solution().roman_to_int("IV"))