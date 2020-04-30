def seq(inp):
    print("---------")
    print("|", " ".join(inp[0:3]), "|")
    print("|", " ".join(inp[3:6]), "|")
    print("|", " ".join(inp[6:9]), "|")
    print("---------")

def whowon(inp, var):
    win = []
    for x in wins:
        win.append(len([y for y in x if inp[y] == var]))
    return win.count(3)

ini = list(input().replace(" ", "_"))
seq(ini)

wins = [[0, 4, 8], [2, 4, 6], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]

x_win = whowon(ini,"X")
y_win = whowon(ini,"O")

if abs(ini.count("X") - ini.count("O")) >= 2 or (x_win == 1 and y_win == 1):
    print("Impossible")
elif x_win == 1:
    print("X wins")
elif y_win == 1:
    print("O wins")
elif x_win == 0 and y_win == 0 and ini.count("_") != 0:
    print("Game not finished")
else:
    print("Draw")
