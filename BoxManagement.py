class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = size
        self.revealed = False
        self.mined = False
        self.flagged = False
        self.value = 0

    def reveal(self):
        self.revealed = True

    def flag(self):
        self.flagged = True

    def set_mine(self):
        self.is_mine = True

    def set_value(self, value):
        self.value = value

    def is_revealed(self):
        return self.revealed
    
    def is_mine(self):
        return self.mined

    def is_flagged(self):
        return self.flagged