## TIC TAC TOE ##


#checks if input is valid (ie. a number between or at 1 and 9)
def check(num, arr, boolean):
    #is the input a + number numeric?
    if (not(num.isnumeric())):
        print("Invalid input, enter again")
        print()
        ins(arr,boolean)
        #is input a number between or at 1 and 9?
    if (int(num) < 1 or int(num) > 9):
        print()
        print("Invalid input, enter again")
        ins(arr,boolean)

#Checks to see if a player has won; goes through all 8 possible win combinations 
def win(a):
    if (a[0][0] == "X" and a[0][1] == "X" and a[0][2] == "X") or (a[1][0] == "X" and a[1][1] == "X" and a[1][2] == "X") or (a[2][0] == "X" and a[2][1] == "X" and a[2][2] == "X") or (a[0][0] == "X" and a[1][0] == "X" and a[2][0] == "X") or (a[0][1] == "X" and a[1][1] == "X" and a[2][1] == "X") or (a[0][2] == "X" and a[1][2] == "X" and a[2][2] == "X") or (a[0][0] == "X" and a[1][1] == "X" and a[2][2] == "X") or (a[0][2] == "X" and a[1][1] == "X" and a[2][0] == "X"):
        return 0
    elif (a[0][0] == "O" and a[0][1] == "O" and a[0][2] == "O") or (a[1][0] == "O" and a[1][1] == "O" and a[1][2] == "O") or(a[2][0] == "O" and a[2][1] == "O" and a[2][2] == "O") or(a[0][0] == "O" and a[1][0] == "O" and a[2][0] == "O") or (a[0][1] == "O" and a[1][1] == "O" and a[2][1] == "O") or (a[0][2] == "O" and a[1][2] == "O" and a[2][2] == "O") or (a[0][0] == "O" and a[1][1] == "O" and a[2][2] == "O")or (a[0][2] == "O" and a[1][1] == "O" and a[2][0] == "O"):
        return 1
    return 2

#Replaces a number on our gird with either X or O depending on whose turn it is
def replace(num, arr, boolean):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == int(num):
                if boolean == False:
                    arr[i][j] = "X"
                else:
                    arr[i][j] = "O"
    show(arr)
    return arr

#Takes input from user, call itself each time until a player has won 
def ins(arr, boolean):
    i = win(arr)
    if i == 0:
        print()
        print("X won!")
        return
    elif i == 1:
        print("O won!")
        return

    if boolean:
        num = input("X position: ")
        check(num, arr, boolean)
        boolean = False
        return ins(replace(num, arr, boolean), boolean)
    else:
        num = input("O position: ")
        check(num, arr, boolean)
        boolean = True
        return ins(replace(num, arr, boolean), boolean)
        

#Displys the board
def show(arr):
    for i in arr:
        m = 0
        for j in i:
            print("",j,"", end="")
            if m < 2:
                print("|", end = "")
                m+=1
        print()
    print()

#main function to run our code 
def main():
    global boolean
    boolean = True
    
    plays = [[1,2,3],[4,5,6],[7,8,9]]
    show(plays)
    ins(plays, boolean)


#running main 
main()
