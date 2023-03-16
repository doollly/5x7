board = [" " for x in range(35)]

def print_board():
    row1 = "| {} | {} | {} | {} | {} |".format(board[0], board[1], board[2], board[3], board[4])
    row2 = "| {} | {} | {} | {} | {} |".format(board[5], board[6], board[7], board[8], board[9])
    row3 = "| {} | {} | {} | {} | {} |".format(board[10], board[11], board[12], board[13], board[14])
    row4 = "| {} | {} | {} | {} | {} |".format(board[15], board[16], board[17], board[18], board[19])
    row5 = "| {} | {} | {} | {} | {} |".format(board[20], board[21], board[22], board[23], board[24])
    row6 = "| {} | {} | {} | {} | {} |".format(board[25], board[26], board[27], board[28], board[29])
    row7 = "| {} | {} | {} | {} | {} |".format(board[30], board[31], board[32], board[33], board[34])

    print()
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print(row6)
    print(row7)
    print()

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-35): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")
         if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon and board[3] == icon and board[4] == icon) or \
       (board[5] == icon and board[6] == icon and board[7] == icon and board[8] == icon and board[9] == icon) or \
       (board[10] == icon and board[11] == icon and board[12] == icon and board[13] == icon and board[14] == icon) or \
       (board[15] == icon and board[16] == icon and board[17] == icon and board[18] == icon and board[19] == icon) or \
       (board[20] == icon and board[21] == icon and board[22] == icon and board[23] == icon and board[24] == icon) or \
       (board[25] == icon and board[26] == icon and board[27] == icon and board[28] == icon and board[29] == icon) or \
       (board[30] == icon and board[31] == icon and board[32] == icon and
