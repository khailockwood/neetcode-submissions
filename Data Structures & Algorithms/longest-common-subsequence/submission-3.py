class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}
        def compare(index1, index2, cache):
            if index1 == len(text1) and index2 == len(text2):
                return 0

            if index1 == len(text1):
                return 0

            if index2 == len(text2):
                return 0

            if (index1, index2) in cache:
                return cache[(index1, index2)]

            if text1[index1] == text2[index2]:
                index1 += 1
                index2 += 1
                return 1 + compare(index1, index2, cache)
            else:
                cache[(index1, index2)] = max(compare(index1, index2 + 1, cache), compare(index1 + 1, index2, cache))
                return cache[(index1, index2)]

        return compare(0, 0, cache)
