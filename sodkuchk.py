correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def validSolution(board):
    # check rows
    for row in board:
        if sorted(row) != correct:
            return False
    
    # check columns
    for column in zip(*board):
        if sorted(column) != correct:
            return False
    
    # check regions
    for i in range(3):
        for j in range(3):
            region = []
            for line in board[i*3:(i+1)*3]:
                region += line[j*3:(j+1)*3]
            
            if sorted(region) != correct:
                return False
    
    # if everything correct
    return True




def valid_solution(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    for i in range(9):
        if len(set(board[i])) != 9:
            return False
        if len(set([board[j][i] for j in range(9)])) != 9:
            return False
    for i in range(3):
        for j in range(3):
            if len(set([board[x][y] for x in range(i*3,i*3+3) for y in range(j*3,j*3+3)])) != 9:
                return False
    return True


