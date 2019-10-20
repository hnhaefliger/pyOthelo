def possibleMoves(color, board):
    opposites = {
            'w': 'b',
            'b': 'w'
            }
    tests = [[1, 1], [0, 1], [1, 0], [-1, -1], [0, -1], [-1, 0], [-1, 1], [1, -1]]
    opposite = opposites[color]
    moves, detail = [], []
    for row in enumerate(board):
        for column in enumerate(row[1]):
            if column[1] == 'e':
                temp = []
                found = False
                for test in tests:
                    if not(any([test[0] + row[0] > 7,
                            test[0] + row[0] < 0,
                            test[1] + column[0] > 7,
                            test[1] + column[0] < 0])):
                        if board[row[0]+test[0]][column[0]+test[1]] == opposite:
                            tempa = []
                            length = 0
                            for x in range(1, 8):
                                try:
                                    a = board[row[0] + test[0]*x][column[0] + test[1]*x]
                                    length += 1
                                except:
                                    break
                                
                            for x in range(1, length):
                                if board[row[0] + test[0]*x][column[0] + test[1]*x] == opposite:
                                    tempa.append([column[0] + test[1]*x, row[0] + test[0]*x])
                                    
                                elif board[row[0] + test[0]*x][column[0] + test[1]*x] == color:
                                    found = True
                                    temp += tempa
                                    break
                                
                                elif board[row[0] + test[0]*x][column[0] + test[1]*x] == 'e':
                                    break
                                
                if found:
                    moves.append([column[0], row[0]])
                    detail.append(temp)

    return moves, detail
