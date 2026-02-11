# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string ""

class Solution:
    def longest_common_prefix(self, strs) -> str:
        strs.sort()

        first = strs[0]
        last = strs[-1]
        length = min(len(first), len(last))

        i = 0
        while i < length and first[i] == last[i]:
            i += 1

        return first[:i]

print(Solution().longest_common_prefix(["flower", "flow", "flight"]))