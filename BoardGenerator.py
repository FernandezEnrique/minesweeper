import random
from BoxManagement import Box

class BoardGenerator:

    def __init__(self, difficulty, num_mines=None, num_boxes_vertical=None, num_boxes_horizontal=None):

        
        if difficulty == "beginner":
            self.num_mines = 10
            self.num_boxes_vertical = 8
            self.num_boxes_horizontal = 8 
        elif difficulty == "medium":
            self.num_mines = 40
            self.num_boxes_vertical = 16
            self.num_boxes_horizontal = 16
        elif difficulty == "advanced":
            self.num_mines = 99
            self.num_boxes_vertical = 30
            self.num_boxes_horizontal = 16
        else:
            self.num_mines = num_mines
            self.num_boxes_vertical = num_boxes_vertical
            self.num_boxes_horizontal = num_boxes_horizontal

        self.board = []
        for i in range(self.num_boxes_vertical):
            row = []
            for j in range(self.num_boxes_horizontal):
                row.append(Box(i,j))
            self.board.append(row)

        self.num_mines_placed = 0

        while self.num_mines_placed < self.num_mines:
            x = random.randint(0, self.num_boxes_horizontal-1)
            y = random.randint(0, self.num_boxes_vertical-1)
           

            self.board.place_mine(x,y)

    def check_box(self, x, y):
        return self.board[x][y].is_mine()

    def place_mine(self, x, y):
        box = self.board[x][y]
         if not box.is_mine():
            box.set_mine()
            self.num_mines_placed += 1
            for i in range(max(0, x-1), min(x+2, self.num_boxes_horizontal)):
                for j in range(max(0, y-1), min(y+2, self.num_boxes_vertical)):
                    neighbor_box = self.board[i][j]
                    if not neighbor_box.is_mine():
                        neighbor_box.set_value(neighbor_box.value + 1)
        
