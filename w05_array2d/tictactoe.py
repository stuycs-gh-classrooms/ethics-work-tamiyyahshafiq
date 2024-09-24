def tictactoe():
    board = [["-"]*3 for i in range(3)]
    
    player1 = input("Who is player one? ")
    print("Player 1: " + player1)
    print("\n")
    
    player2 = input("Who is player two? ")
    print("Player 2: " + player2)
    print("\n")
    
    print("This is the playing board:")
    print(board[0])
    print(board[1])
    print(board[2])
    
    for i in range(9):
        player = input("What player are you? 1 or 2 ")
        row = input("What row would you like to place yourself in? ")
        col = input("What column would you like to place yourself in? ")
                
        if (player == "1" and (board[int(row)-1][int(col)-1] == "-")):
            board[int(row)-1][int(col)-1] = "X"
        
        if (player == "2" and (board[int(row)-1][int(col)-1] == "-")):
            board[int(row)-1][int(col)-1] = "O"
            
        if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != "-"):
            print(board[0][0] + " won!")
            return
        
        elif (board[1][0] == board[1][1] == board[1][2] and board[1][0] != "-"):
            print(board[1][0] + " won!")
            return
        
        elif (board[2][0] == board[2][1] == board[2][2] and board[2][0] != "-"):
            print(board[2][0] + " won!")
            return
        
        elif (board[0][0] == board[1][0] == board[2][0] and board[0][0] != "-"):
            print(board[0][0] + " won!")
            return
        
        elif (board[0][1] == board[1][1] == board[2][1] and board[0][1] != "-"):
            print(board[0][1] + " won!")
            return
        
        elif (board[0][2] == board[1][2] == board[2][2] and board[0][2] != "-"):
            print(board[0][2] + " won!")
            return
        
        elif (board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-"):
            print(board[0][0] + " won!")
            return
        
        elif (board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-"):
            print(board[0][2] + " won!")
            return
        
        print(board[0])
        print(board[1])
        print(board[2])
        
    print("No one won.")

tictactoe()
