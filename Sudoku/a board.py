grid = [[0 for x in range(9)] for y in range(9)]


# show board
def show_board():
    for i in range(9):
        if i % 3 == 0:
            print("- - - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0:
                print('|', end = ' ')
            print(grid[i][j], end = ' ')

        print("|")

    print("- - - - - - - - - - - - -")


# checking validity of @val in (X,Y) position
def valid_check(X, Y, val):
    for i in range(9):
        for j in range(9):
            if (i == X or j == Y) and grid[i][j] == val:
                return False

    x_start, y_start = X // 3, Y // 3
    x_start *= 3
    y_start *= 3

    # checking 3*3 sub grids
    for i in range(x_start, x_start + 3):
        for j in range(y_start, y_start + 3):
            if grid[i][j] == val:
                return False
    return True


def generate_board():
    if sum(i.count(0) for i in grid):
        x, y = -1, -1
        for x_pos in range(9):
            for y_pos in range(9):
                if grid[x_pos][y_pos] == 0:
                    x, y = x_pos, y_pos
                    break
            if x != -1 and y != -1:
                break

        if x != -1 and y != -1:
            for val in range(1, 10):
                if valid_check(x, y, val):
                    grid[x][y] = val
                    generate_board()
                    grid[x][y] = 0

    else:
        show_board()
        exit(0)


generate_board()
