grid = [[0 for x in range(9)] for y in range(9)]


class sudoku:

    def __init__(self):
        grid = [[0 for x in range(9)] for y in range(9)]

    def show_board(self):
        for i in range(9):
            if i % 3 == 0:
                print("- - - - - - - - - - - - -")
            for j in range(9):
                if j % 3 == 0:
                    print('|', end = ' ')
                print(grid[i][j], end = ' ')

            print("|")

        print("- - - - - - - - - - - - -")


