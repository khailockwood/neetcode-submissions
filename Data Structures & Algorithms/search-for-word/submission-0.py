from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #find starting point
        #dfs, check each neighbor, go down the path of each neighbor
        #don't append: if out of bounds, if not next letter
        rows = len(board)
        cols = len(board[0])

        currPath = set()

        def dfs(r, c, currPath, goalWord):
            if r >= rows or c >= cols or r < 0 or c < 0 or board[r][c] != goalWord[0] or (r, c) in currPath:
                return False
            elif len(goalWord) == 1:
                return True
            else:
                currPath.add((r, c))
                goalWord = goalWord[1:]
                res = dfs(r + 1, c, currPath, goalWord) or dfs(r - 1, c, currPath, goalWord) or dfs(r, c + 1, currPath, goalWord) or dfs(r, c - 1, currPath, goalWord)
                currPath.remove((r, c))
                return res
                
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = dfs(i, j, currPath, word)
                    if res:
                        return True
        return False




        

