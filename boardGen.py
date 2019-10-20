import tkinter, os

class board:
    def create_piece(self, x, y, color):
        self.squares[y][x] = self.board.create_oval(x*80+10, y*80+10, x*80+70, y*80+70, fill=color)

    def highlight(self, x, y):
        self.board.itemconfig(self.boardsquares[y][x], fill='lightblue')

    def unhighlight(self, x, y):
        if x % 2 == y % 2:
            self.board.itemconfig(self.boardsquares[y][x], fill='#b3b3b3')
        else:
            self.board.itemconfig(self.boardsquares[y][x], fill='#666666')

    def select(self, x, y):
        self.board.itemconfig(self.boardsquares[y][x], fill='green')

    def unselect(self, x, y):
        if x % 2 == y % 2:
            self.board.itemconfig(self.boardsquares[y][x], fill='#b3b3b3')
        else:
            self.board.itemconfig(self.boardsquares[y][x], fill='#666666')

    def mark(self, x, y):
        self.board.itemconfig(self.boardsquares[y][x], fill='red')

    def unmark(self, x, y):
        if x % 2 == y % 2:
            self.board.itemconfig(self.boardsquares[y][x], fill='#b3b3b3')
        else:
            self.board.itemconfig(self.boardsquares[y][x], fill='#666666')

    def destroy(self):
        self.root.destroy()

    def __init__(self, handle):
        self.click = ''

        self.root = tkinter.Tk()
        self.root.geometry('640x640')
        self.root.title('Othelo')

        self.board = tkinter.Canvas(self.root, width=640, height=640)
        self.board.pack()
        
        self.squares = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]

        self.boardsquares = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]

        for x in range(8):
            for y in range(8):
                if x % 2 == y % 2:
                    self.boardsquares[y][x] = self.board.create_rectangle(x*80, y*80, x*80+80, y*80+80, fill='#b3b3b3')
                else:
                    self.boardsquares[y][x] = self.board.create_rectangle(x*80, y*80, x*80+80, y*80+80, fill='#666666')

        self.create_piece(3, 3, 'white')
        self.create_piece(3, 4, 'black')
        self.create_piece(4, 3, 'black')
        self.create_piece(4, 4, 'white')
                    
        self.board.bind('<Button>', handle)
