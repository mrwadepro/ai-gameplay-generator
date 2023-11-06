import pygame
from iter_game import iter_game

class CheckerPiece:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.king = False

class CheckerBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_pieces()

    def initialize_pieces(self):
        for i in range(8):
            for j in range(8):
                if i < 3 and (i+j)%2 == 0:
                    self.board[i][j] = CheckerPiece('BLACK', (i,j))
                elif i > 4 and (i+j)%2 == 0:
                    self.board[i][j] = CheckerPiece('RED', (i,j))

class checkers_game(iter_game):
    def __init__(self, window_width=800, window_height=800):
        super().__init__(window_width, window_height)
        self.board = CheckerBoard()
        self.selected_piece = None
        self.turn = 'BLACK'

    def next(self, pygame, events, screen, dt, data):
        if self.fin:
            data.game_num = 0
            return
        for event in events:
            if event.type == pygame.QUIT:
                self.fin = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // 100, x // 100
                if self.selected_piece:
                    result = self.move_piece(row, col)
                    if not result:
                        self.selected_piece = None
                        self.select_piece(row, col)
                else:
                    self.select_piece(row, col)
        self.draw_board(screen)
        pygame.display.update()

    def select_piece(self, row, col):
        print("select_piece")
        piece = self.board.board[row][col]
        if piece and piece.color == self.turn:
            self.selected_piece = piece

    def move_piece(self, row, col):
        print("huh")
        if self.board.board[row][col] or (row+col)%2:
            return False
        self.board.board[self.selected_piece.pos[0]][self.selected_piece.pos[1]] = None
        self.board.board[row][col] = self.selected_piece
        self.selected_piece.pos = (row, col)
        self.turn = 'RED' if self.turn == 'BLACK' else 'BLACK'
        return True

    def draw_board(self, screen):
        for i in range(8):
            for j in range(8):
                color = (255, 255, 255) if (i+j)%2 == 0 else (0, 0, 0)
                pygame.draw.rect(screen, color, pygame.Rect(j*100, i*100, 100, 100))
                piece = self.board.board[i][j]
                if piece:
                    p_color = (0, 0, 0) if piece.color == 'BLACK' else (255, 0, 0)
                    pygame.draw.circle(screen, p_color, (j*100+50, i*100+50), 45)