import os

GAME_TITLE = "*** Tic Toc Toe ***"
FIELD_DATA = """
  1 2 3
 -------
1|11|12|13|
 -------
2|21|22|23|
 -------
3|31|32|33|
 -------
"""
INPUT_MARK = {
    "0": " ",
    "1": "O",
    "2": "X",
}

def have_empty_position(matrix):
    return any(0 in sublist for sublist in matrix)

def judge_player(matrix, player):
    for row in range(0, 3):
        if matrix[row][0] == player and matrix[row][1] == player and matrix[row][2] == player:
            return True

    for col in range(0, 3):
        if matrix[0][col] == player and matrix[1][col] == player and matrix[2][col] == player:
            return True

    if matrix[0][0] == player and matrix[1][1] == player and matrix[2][2] == player:
        return True
    if matrix[2][0] == player and matrix[1][1] == player and matrix[0][2] == player:
        return True
    
    return False


def judge(matrix):
    """ judge status, return 0:not yet, 1: player1 win, 2: player2 win, 3: draw"""
    if judge_player(matrix, 1):
        return 1
    elif judge_player(matrix, 2):
        return 2
    elif not have_empty_position(matrix):
        return 3
    else:
        return 0

def showstatus(matrix):
    """ show current game status"""
    data = FIELD_DATA
    for i in range(1,4):
        for j in range(1, 4):
            data = data.replace(f"{i}{j}", INPUT_MARK[f"{matrix[i-1][j-1]}"])

    os.system('clear')
    print(GAME_TITLE)
    print(data)

should_continue = True

# hold user input, 0:initial, 1:player1, 2:player2
input_list = [[0,0,0],[0,0,0],[0,0,0]]

showstatus(input_list)

# next turn
next_player = 1

while should_continue:
    # get position
    input_loop = True
    while input_loop:
        position = input(f"[Player {next_player}]Please input position. [1-3][1-3]:\n")
        if len(position) == 2 and\
                (position[0] == "1" or position[0] == "2" or position[0] == "3") and \
                (position[1] == "1" or position[1] == "2" or position[1] == "3"):
            # input position is valid
            x = int(position[0]) - 1
            y = int(position[1]) - 1
            if input_list[x][y] == 0:
                # position is empty
                input_loop = False

    input_list[x][y] = next_player

    # show current status
    showstatus(input_list)

    # judge
    judge_result = judge(input_list)
    if judge_result == 1 or judge_result == 2:
        print(f"Player {next_player} Won!")
        should_continue = False
    elif judge_result == 3:
        print("Draw Game.")
        should_continue = False

    # decide next turn
    if next_player == 1:
        next_player = 2
    else:
        next_player = 1

