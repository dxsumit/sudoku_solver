# sudoku solver using backtracking...

# this one is an example of unsolvable sudoku problem
board = [
    [5,1,6,8,4,9,7,3,2],
    [3," ",7,6," ",5," "," "," "],
    [8," ",9,7," "," "," ",6,5],
    [1,3,5," ",6," ",9," ",7],
    [4,7,2,5,9,1," "," ",6],
    [9,6,8,3,7," "," ",5," "],
    [2,5,3,1,8,6," ",7,4],
    [6,8,4,2," ",7,5," "," "],
    [7,9,1," ",5," ",6," ",8]
]


class sudoku(object):
    def __init__(self, board):
        self.board = board

        # printing board....
        for i in range(9):
            if(i%3 == 0 and i != 0):
                print("-"*21)
        
            for j in range(9):
                if(j%3 == 0 and j != 0):
                    print("| ", end="")
                if(j == 8):
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")


    #  check for empty spaces in board...
    def empty_space(self, board):
        for i in range(9):
            for j in range(9):
                if(board[i][j] == " "):
                    # returing row and column number of that empty space 
                    return (i, j)   

        return False


    # check that inserted number is valid or not..
    def is_valid(self, board, number, position):
        # row
        for i in range(9):
            if(position[1] != i and board[position[0]][i] == number):
                return False

        # column
        for i in range(9):
            if(position[0] != i and board[i][position[1]] == number):
                return False

        # 3*3 box
        box_Y = position[0]//3
        box_X = position[1]//3
        for i in range(box_Y*3, box_Y*3 + 3):
            for j in range(box_X*3, box_X*3 + 3):
                if(board[i][j] == number and (i,j) != position):
                    return False

        return True


    # solving sudoku using recursion..
    def solver(self, board):
        any_space = self.empty_space(board)
        if(not any_space):
            return True
        else:
            row, col = any_space
        
        for i in range(1,10):
            if self.is_valid(board, i, (row,col)):
                board[row][col] = i
                if(self.solver(board)):
                    return True
                # board[row][col] = " "

        return False



obj = sudoku(board)
print("-_"*20, end='\n\n')

if(obj.solver(board)):
    obj.__init__(board)
else:
    print("  Solution for this set of 9X9 sudoku is NOT POSSIBLE ") 

    
    
# end of program


