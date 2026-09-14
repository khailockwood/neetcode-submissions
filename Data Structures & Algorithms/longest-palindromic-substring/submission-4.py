class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIndex = 0
        resLength = 0
        #go to each index, choose that as middle, go outwards on each side to compare chars

        for i in range (len(s)):
            l = i
            r = i
            #try this loop for each over index
            while l >= 0 and r < len(s) and s[l] == s[r]: #while not out of bounds and palindrome condition true
                if (r - l + 1) > resLength: #if current length > maxLength
                    resIndex = l
                    resLength = r - l + 1
                l -= 1 #outward
                r += 1

            l = i
            r = i + 1 #now try the loop for every odd index
            while l >= 0  and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLength:
                    resIndex = l
                    resLength = r - l + 1
                l -= 1
                r += 1

        #we only return how long it is and where it start, so to get string:

        return s[resIndex : resIndex + resLength] #return: splice from starting index to starting index + final palindrome length
    