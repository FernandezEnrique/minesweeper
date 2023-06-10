import pygame
from menu import Menu

from game import *

class Game:
    def __init__(self, mode):
        pygame.init()
        
        #guardamos el modo de juego
        self.mode = mode

        self.mines = 0
        self.boxes_vertical = 0
        self.boxes_horizontal = 0

        if self.mode == "beginner":
            self.mines = 10
            self.boxes_vertical = 8
            self.boxes_horizontal = 8 
        elif self.mode == "medium":
            self.mines = 40
            self.boxes_vertical = 16
            self.boxes_horizontal = 16
        elif self.mode == "advanced":
            self.mines = 99
            self.boxes_vertical = 30
            self.boxes_horizontal = 16
        else:
            self.mines = mines
            self.boxes_vertical = boxes_vertical
            self.boxes_horizontal = boxes_horizontal

        gameInit(self.boxes_vertical, self.boxes_horizontal, self.mines)
        
        self.board = get_board()

        #tamaño de las casillas
        self.box_size = 40

        #definimos las dimensiones de la pantalla de pygame
        self.width = self.box_size * self.boxes_horizontal
        self.height = self.box_size * self.boxes_vertical
        self.screen = pygame.display.set_mode((self.width, self.height))


        pygame.display.set_caption("Minesweeper")
        pygame.display.update()

        #imagenes
        self.mine_img = pygame.image.load('img/mine.png') # Carga la imagen de la mina
        self.mine_img = pygame.transform.scale(self.mine_img, (self.box_size, self.box_size)) # Escala la imagen al tamaño de las casillas
        
        self.flag_img = pygame.image.load('img/green_flag.jpg') # Carga la imagen de la mina
        self.flag_img = pygame.transform.scale(self.flag_img, (self.box_size, self.box_size))

        self.font = pygame.font.SysFont(None, 30)


        #futuro icono
        #self.icon = pygame.image.load('img/x_minib.png')
        #pygame.display.set_icon(self.icon)

    def start(self):
        print_board()
        while  gameGetState() == STATE_GOING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_RIGHT:
                    pos = pygame.mouse.get_pos()
                    self.handle_right_click(pos)
                elif  event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.handle_left_click(pos)

            self.draw_board()

            pygame.display.update()

    
    def handle_left_click(self, pos):
        x, y = pos[1] // self.box_size, pos[0] // self.box_size
        gameClearCell(x,y)
        
        
    
    def handle_right_click(self, pos):
        x, y = pos[1] // self.box_size, pos[0] // self.box_size

        gameFlagCell(x,y)
    
    
    def draw_board(self):
        self.screen.fill((255, 255, 255))
        
        for i in range(self.boxes_vertical):
            for j in range(self.boxes_horizontal):
                box = self.board[i][j]
                x, y = j * self.box_size, i * self.box_size

                if check_clear(box):
                    
                    if check_mine(box):
                        self.screen.blit(self.mine_img, (x, y))
                    
                    else:
                        pygame.draw.rect(self.screen, (200, 200, 200), (x, y, self.box_size, self.box_size))
                        n = count_neighbor_mines(i,j)
                        if n > 0:
                            text = self.font.render(str(n), True, (0, 0, 0))
                            text_rect = text.get_rect(center=(x + self.box_size // 2, y + self.box_size // 2))
                            self.screen.blit(text, text_rect)

                
                
                elif check_flag(box):
                    self.screen.blit(self.flag_img, (x, y))
                

                else:
                    pygame.draw.rect(self.screen, (150, 150, 150), (x, y, self.box_size, self.box_size))
                
                
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, self.box_size, self.box_size), 1)
                if j == self.boxes_horizontal - 1:
                    pygame.draw.line(self.screen, (0, 0, 0), (x + self.box_size, y), (x + self.box_size, y + self.box_size), 1)
                if i == self.boxes_vertical - 1:
                    pygame.draw.line(self.screen, (0, 0, 0), (x, y + self.box_size), (x + self.box_size, y + self.box_size), 1)

        if  gameGetState() == STATE_LOST:
            self.running = False
            mode = Menu("Menu", "Has perdido, desea jugar de nuevo?", "Yes", "No")
            if ( mode.selection == "Yes"):
                mode = Menu("Menu", "Choose game mode", "beginner", "medium", "advanced", "personalized" )
                if ( mode.selection == "beginner"):
                    Game("beginner").start()
                elif ( mode.selection == "medium"):
                    Game("medium").start()
                elif ( mode.selection == "advanced"):
                    Game("advanced").start()
                else:
                    Game("personalized").start()


        
        elif  gameGetState() == STATE_WON:
            mode = Menu("Menu", "Choose game mode", "beginner", "medium", "advanced", "personalized" )
            if ( mode.selection == "beginner"):
                Game("beginner").start()
            elif ( mode.selection == "medium"):
                Game("medium").start()
            elif ( mode.selection == "advanced"):
                Game("advanced").start()
            else:
                Game("personalized").start()
    


if __name__ == "__main__":
    mode = Menu("Menu", "Choose game mode", "beginner", "medium", "advanced", "personalized" )
    if ( mode.selection == "beginner"):
        Game("beginner").start()
    elif ( mode.selection == "medium"):
        Game("medium").start()
    elif ( mode.selection == "advanced"):
        Game("advanced").start()
    else:
        Game("personalized").start()
    