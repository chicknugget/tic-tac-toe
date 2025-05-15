import numpy as np
import re
import random

checkboard=np.array([["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]])
chshow=np.array([[" A1 ", " A2 ", " A3 "], [" B1 ", " B2 ", " B3 "], [" C1 ", " C2 ", " C3 "]])

def main():
    rules()
    choice=int(input("How would you like to play?\n1. With the Computer\n2. With a Friend(Multiplayer)\n\n"))
    if choice==1:
        check()
        while True:
            ask_user1("")
            if winner() == "X":
                check()
                print("Congratulations! You win!")
                break
            if is_draw():
                check()
                print("It's a draw!")
                break

            ask_computer()
            if winner() == "O":
                check()
                print("Computer wins! Better luck next time.")
                break
            if is_draw():
                check()
                print("It's a draw!")
                break
            check()
    elif choice==2:
        name1=input("Name for player number 1: ")
        name2=input("Name for player number 2: ")
        check()
        while True:
            ask_user1(name1)
            if winner() == "X":
                check()
                print(f"Congratulations {name1} wins!")
                break
            if is_draw():
                check()
                print("It's a draw!")
                break

            ask_user2(name2)
            if winner() == "O":
                check()
                print(f"Congratulations {name2} wins!")
                break
            if is_draw():
                check()
                print("It's a draw!")
                break
            check()
    else:
        print("Invalid Entry")

def rules():
    print("-"*45+"WELCOME TO A CLASSIC GAME OF TICTACTOE"+ "-"*45)
    print("\nHere are the rules:\n\n-->The goal of Tic Tac Toe is to be the first player to align three of your symbols (either X or O) in a row, which can be done vertically, horizontally, or diagonally.")
    print("\n-->The board looks like this:")
    print("    1    2    3  ")
    print(" ----------------")
    for i in range(3):
        row_label = chr(65 + i)
        print(f"{row_label}|", end="")
        for j in range(3):
            print(f"{chshow[i][j]}|", end="")
        print("\n ----------------")
    print("\n-->A player wins by placing three of their symbols in a row (horizontally, vertically, or diagonally).\n")
    print("Enjoy your game :)\n\n")


def check():
    print("   1   2   3  ")
    print(" -------------")
    for i in range(3):
        row_label = chr(65 + i)
        print(f"{row_label}|", end="")
        for j in range(3):
            print(f"{checkboard[i][j]}|", end="")
        print("\n -------------")

def ask_user1(name):
    while True:
        try:
            x=input(f"Enter your choice {name}: ")
            x=x.upper()
            checkask=re.search(r"^[A-C]{1}[1-3]{1}$", x)
            if not checkask:
                raise ValueError("Invalid format!")

            i = ord(x[0])-65
            j = int(x[1])-1

            if checkboard[i][j] != "   ":
                print("Oops! That position is taken! Try Again.")
                continue

            checkboard[i][j] = " X "
            break
        except (ValueError, IndexError):
            print("Invalid Entry! Try Again.")

def ask_user2(name):
    while True:
        check()
        try:
            o=input(f"Enter your choice {name}: ")
            o=o.upper()
            checkask=re.search(r"^[A-C]{1}[1-3]{1}$", o)
            if not checkask:
                raise ValueError("Invalid format!")

            i=ord(o[0])-65
            j=int(o[1])-1

            if checkboard[i][j] != "   ":
                print("Oops! That position is taken! Try Again.")
                continue

            checkboard[i][j] = " O "
            break
        except (ValueError, IndexError):
            print("Invalid Entry! Try Again.")

def ask_computer():
    available_moves = [(i, j) for i in range(3) for j in range(3) if checkboard[i][j] == "   "]
    if available_moves:
        i, j = random.choice(available_moves)
        checkboard[i][j] = " O "
        print(f"Computer chose: {chr(i + 65)}{j + 1}")

def winner():
    for i in range(3):
        if np.all(checkboard[i] == " X ") or np.all(checkboard[:, i] == " X "):
            return "X"
        if np.all(checkboard[i] == " O ") or np.all(checkboard[:, i] == " O "):
            return "O"
    if checkboard[0][0] == checkboard[1][1] == checkboard[2][2]:
        return checkboard[0][0].strip()
    if checkboard[0][2] == checkboard[1][1] == checkboard[2][0]:
        return checkboard[0][2].strip()
    return None

def is_draw():
    return np.all(checkboard != "   ")


if __name__ == "__main__":
    main()
