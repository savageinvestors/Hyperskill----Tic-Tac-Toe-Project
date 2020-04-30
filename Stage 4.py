user_input = list(input("Enter cells: "))
matrix = []
k = 0
def show():
    global matrix
    print("---------")
    for i in range(0, 3):
        print("|", end="")
        for j in range(0, 3):
            print(" " + matrix[i][j], end="")
        print(" |")
    print("---------")

for i in range (0,3):
    matrix.append([])
    for j in range (0,3):
        matrix[i].append(user_input[k])
        k += 1

show()

while True:
    x, y = input("Enter the coordinates: ").split()
    try:
        x = int(x)
        y = int(y)
        if x < 1 or y > 3 or x < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            if matrix[abs(y-3)][abs(x-1)] == "_":
                matrix[abs(y-3)][abs(x-1)] = "X"
                show()
                break
            else:
                print("This cell is occupied! Choose another one!")
    except:
        print("You should enter numbers!")
