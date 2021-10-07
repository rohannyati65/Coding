# 79. Word Search (leetcode)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(board, word, row, col, pos):
            if pos == len(word):
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            if board[row][col] == "*":
                return False
            if board[row][col] == word[pos]:
                temp = board[row][col]
                board[row][col] = "*"
                if check(board, word, row + 1, col, pos + 1) == True:
                    return True
                elif check(board, word, row - 1, col, pos + 1) == True:
                    return True
                elif check(board, word, row, col + 1, pos + 1) == True:
                    return True
                elif check(board, word, row, col - 1, pos + 1) == True:
                    return True
                board[row][col] = temp

            return False

        pos = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(board, word, i, j, pos):
                    return True
        return False
