class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #as soon as we see a duplicate, we store length of substring before, then start over tracking substring with earlier duplicate and everything before it removed
        #hashmap tracking indices for each char

        start = 0
        hashMap = {}
        longest = 0

        for i in range(len(s)):
            if s[i] in hashMap: # we see a dpublicate, move the start of our sliding window past it
                if hashMap[s[i]] + 1 > start: 
                    start = hashMap[s[i]] + 1

            hashMap[s[i]] = i #map each char to its index so we can easily move our sliding window

            if (i - start + 1) > longest: #if the length of our sliding window > longest
                longest = i - start + 1
        
        return longest

