# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            currGuess = (left + right) // 2
            print(currGuess)
            if guess(currGuess) == 0:
                return currGuess
            if guess(currGuess) == -1:
                right = currGuess - 1
            elif guess(currGuess) == 1:
                left = currGuess + 1
        return currGuess
            
