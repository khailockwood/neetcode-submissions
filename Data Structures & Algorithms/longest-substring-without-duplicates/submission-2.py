class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #as soon as we see a duplicate, we store length of substring before, then start over tracking substring with earlier duplicate and everything before it removed
        #hashmap tracking indices for each char

        start = 0
        hashMap = {}
        longest = 0

        for i in range(len(s)):
            if s[i] in hashMap:
                start = max(hashMap[s[i]] + 1, start)
            hashMap[s[i]] = i
            longest = max(longest, i - start + 1)
        
        return longest

