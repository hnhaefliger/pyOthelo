import boardGen, moves

def play(event):
    global selection, turn, possible_moves, detail, main, plays
    x = int((event.x - event.x % 80) / 80)
    y = int((event.y - event.y % 80) / 80)

    if [x, y] == selection:
        opposites = {
            'w': 'b',
            'b': 'w'
            }
        colors = {
            'w': 'white',
            'b': 'black'
            }

        main.unselect(x, y)
        main.highlight(x, y)
        for move in possible_moves:
            main.unhighlight(move[0], move[1])
        
        main.create_piece(x, y, colors[turn])
        board[y][x] = turn

        move = possible_moves.index([x, y])
        for square in detail[move]:
            board[square[1]][square[0]] = turn
            main.create_piece(square[0], square[1], colors[turn])
            main.unmark(square[0], square[1])

        plays += 1
        turn = opposites[turn]
        selection = ''

        possible_moves, detail = moves.possibleMoves(turn, board)

        if plays == 64:
            scores = {
                    'w': 0,
                    'b': 0
                    }
            for row in board:
                for column in row:
                    scores[column] += 1
            color = scores.index(max(scores['b'], scores['w']))
            print(colors[color], 'Wins!')
            main.destroy()
            
        elif possible_moves == []:
            print(colors[opposites[turn]], 'Wins!')
            main.destroy()

        for move in possible_moves:
            main.highlight(move[0], move[1])
        
    elif [x, y] in possible_moves:
        if selection != '':
            main.unselect(selection[0], selection[1])
            main.highlight(selection[0], selection[1])
            
            move = possible_moves.index([selection[0], selection[1]])
            for square in detail[move]:
                main.unmark(square[0], square[1])
                
        selection = [x, y]
        move = possible_moves.index([x, y])
        for square in detail[move]:
            main.mark(square[0], square[1])
        main.unhighlight(x, y)
        main.select(x, y)

board = [['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
         ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
         ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
         ['e', 'e', 'e', 'w', 'b', 'e', 'e', 'e'],
         ['e', 'e', 'e', 'b', 'w', 'e', 'e', 'e'],
         ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
         ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
         ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
         ]
                           
global selection, turn, possible_moves, detail, main, plays
turn = 'w'
plays = 0
selection = ''
possible_moves, detail = moves.possibleMoves(turn, board)
main = boardGen.board(play)

for move in possible_moves:
    main.highlight(move[0], move[1])

main.root.mainloop()
