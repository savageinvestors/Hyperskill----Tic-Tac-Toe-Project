def print_matrix():
    k = 2
    print("---------")
    while k >= 0:
        print("| " + Matrix[0][k] + " " + Matrix[1][k] + " " + Matrix[2][k] + " |")
        k -= 1
    print("---------")
Matrix = [[x for x in range(3)] for y in range(3)]
for i in range(2, -1, -1):
    for j in range(3):
        Matrix[j][i] = ' '
check_list = []
k = 0
def print_coordinates():
    global k
    global x
    global o
    global coordinates
    coordinates = input("Enter the coordinates: ").split()
    try:
        coor1 = int(coordinates[0]) - 1
        coor2 = int(coordinates[1]) - 1
        if coor1 > 2 or coor2 > 2:
            print("Coordinates should be from 1 to 3!")
            print_coordinates()
        elif Matrix[coor1][coor2] == "X" or Matrix[coor1][coor2] == "O":
            print("This cell is occupied! Choose another one!")
            print_coordinates()
        elif Matrix[coor1][coor2] == " ":
            if x == True and o == False:
                Matrix[coor1][coor2] = "X"
                x = False
                o = True
                k += 1
                print_matrix()
                check(Matrix)
            elif x == False and o == True:
                Matrix[coor1][coor2] = "O"
                o = False
                x = True
                k += 1
                print_matrix()
                check(Matrix)
    except ValueError:
        print("You should enter numbers!")
        print_coordinates()
def check(l):
    if l[0][0] == l[1][0] == l[2][0] and l[0][0] != " ":
        check_list.append(l[0][0])
    if l[0][1] == l[1][1] == l[2][1] and l[0][1] != " ":
        check_list.append(l[0][1])
    if l[0][2] == l[1][2] == l[2][2] and l[0][2] != " ":
        check_list.append(l[0][2])
    if l[0][0] == l[0][1] == l[0][2] and l[0][0] != " ":
        check_list.append(l[0][0])
    if l[1][0] == l[1][1] == l[1][2] and l[1][0] != " ":
        check_list.append(l[1][0])
    if l[2][0] == l[2][1] == l[2][2] and l[2][0] != " ":
        check_list.append(l[2][0])
    if l[0][0] == l[1][1] == l[2][2] and l[0][0] != " ":
        check_list.append(l[0][0])
    if l[0][2] == l[1][1] == l[2][0] and l[0][2] != " ":
        check_list.append(l[0][2])
    if len(check_list) == 2:
        print("Impossible")
    elif len(check_list) == 1:
        print(check_list[0] + " wins")
    elif len(check_list) == 0 and k < 9:
        print_coordinates()
    elif len(check_list) == 0 and k == 9:
        print("Draw")
print_matrix()
coordinates = []
x = True
o = False
print_coordinates()
