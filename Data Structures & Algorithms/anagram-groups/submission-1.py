class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCounts = []
        sortedWords = {}
        for string in strs:
            newWord = "".join(sorted(string))
            if (newWord) in sortedWords:
                sortedWords[newWord].append(string)
            else:
                sortedWords[newWord] = [string]

        finalArray = []
        
        for key in sortedWords:
            finalArray.append(sortedWords[key])

        return finalArray