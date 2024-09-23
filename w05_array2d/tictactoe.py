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
        player = input("What player are you? 1 or 2")
        row = input("What row would you like to place yourself in?")
        col = input("What column would you like to place yourself in?")
        
        if (player == "1"):
            board[int(row)-1][int(col)-1] = "X"
        
        if (player == "2"):
            board[int(row)-1][int(col)-1] = "O"
        
        print(board)

tictactoe()
