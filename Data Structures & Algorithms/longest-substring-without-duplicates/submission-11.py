class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        left = 0
        charMap = {}
        for i in range(len(s)):
            if s[i] not in charMap:
                charMap[s[i]] = i
            else:
                left = max(left, charMap[s[i]] + 1)
                charMap[s[i]] = i

            if (i - left + 1)> longest:
                longest = i - left + 1

        return longest
