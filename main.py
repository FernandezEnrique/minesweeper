import pygame
from BoardGenerator import BoardGenerator
from BoxManagement import Box
from menu import Menu

class Game:
    def __init__(self, mode):
        pygame.init()
        
        #guardamos el modo de juego
        self.mode = mode

        #creamos el tablero
        self.board = BoardGenerator(self.mode)
        self.num_mines = self.board.num_mines
        self.num_boxes_vertical = self.board.num_boxes_vertical
        self.num_boxes_horizontal = self.board.num_boxes_horizontal

        #tamaño de las casillas
        self.box_size = 40

        #definimos las dimensiones de la pantalla de pygame
        self.width = self.box_size * self.board.num_boxes_horizontal
        self.height = self.box_size * self.board.num_boxes_vertical
        self.screen = pygame.display.set_mode((self.width, self.height))


        pygame.display.set_caption("Minesweeper")
        pygame.display.update()
        
        self.running = True
        self.game_over = False
        self.game_won = False

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
        self.board.print_board()
        while not self.game_over and not self.game_won and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_RIGHT:
                    pos = pygame.mouse.get_pos()
                    self.handle_right_click(pos)
                elif  event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.handle_left_click(pos)

            self.draw_board()

            pygame.display.update()

    #gestiona el click izquierdo
    def handle_left_click(self, pos):
        x, y = pos[1] // self.box_size, pos[0] // self.box_size

        box = self.board.board[x][y]

        #si la casilla no esta revelada y no es una bandera
        if not box.is_revealed() and not box.is_flagged():
            #si es mina, se acaba eljuego
            if box.is_mine():
                self.game_over = True
            #si no la revelamos
            else:
                box.reveal()
        
        #comprobamos victoria
        self.check_win()

    #gestiona el click derecho
    def handle_right_click(self, pos):
        x, y = pos[1] // self.box_size, pos[0] // self.box_size

        box = self.board.board[x][y]

        #si no esta revelada y no hay una bandera, la colocamos
        if not box.is_revealed() and not box.is_flagged():
            box.flag()
        elif box.is_flagged():
            box.unflag()
    
    #comprueba si se ha ganado
    def check_win(self):
        revealed_boxes = 0

        #cuenta cuantas casillas se han revelado
        for i in range(self.num_boxes_vertical):
            for j in range(self.num_boxes_horizontal):
                if self.board.board[i][j].is_revealed():
                    revealed_boxes += 1
        
        #si ese numero es igual al total de casillas menos las minas has ganado
        if revealed_boxes == self.num_boxes_horizontal * self.num_boxes_vertical - self.num_mines:
            self.game_won = True
    
    #dibuja el tablero
    def draw_board(self):
        self.screen.fill((255, 255, 255))
        
        for i in range(self.num_boxes_vertical):
            for j in range(self.num_boxes_horizontal):
                box = self.board.board[i][j]
                x, y = j * self.box_size, i * self.box_size

                if box.is_revealed():
                    #si es una mina la mostramos
                    if box.is_mine():
                        self.screen.blit(self.mine_img, (x, y))
                    #si no es mina y esta revelada, pintamos el valor
                    else:
                        pygame.draw.rect(self.screen, (200, 200, 200), (x, y, self.box_size, self.box_size))
                        if box.value > 0:
                            text = self.font.render(str(box.value), True, (0, 0, 0))
                            text_rect = text.get_rect(center=(x + self.box_size // 2, y + self.box_size // 2))
                            self.screen.blit(text, text_rect)

                
                #si no esta revelada pero si contiene una bandera, la mostramos
                elif box.is_flagged():
                    self.screen.blit(self.flag_img, (x, y))
                
                #si no se pinta normal   
                else:
                    pygame.draw.rect(self.screen, (150, 150, 150), (x, y, self.box_size, self.box_size))
                
                #pinta la cuadricula
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, self.box_size, self.box_size), 1)
                if j == self.num_boxes_horizontal - 1:
                    pygame.draw.line(self.screen, (0, 0, 0), (x + self.box_size, y), (x + self.box_size, y + self.box_size), 1)
                if i == self.num_boxes_vertical - 1:
                    pygame.draw.line(self.screen, (0, 0, 0), (x, y + self.box_size), (x + self.box_size, y + self.box_size), 1)

        if self.game_over:
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


        #si se gana, se muestra el menu
        elif self.game_won:
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
    