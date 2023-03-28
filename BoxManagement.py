class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        #indica si la casilla esta revelada
        self.revealed = False

        #indica si la casilla contiene una mina
        self.mined = False

        #indica si hay un bandera en la casilla
        self.flagged = False

        #indica el valor de la casilla
        self.value = 0

    #revela una casilla
    def reveal(self):
        self.revealed = True

    #coloca una bandera
    def flag(self):
        self.flagged = True
        self.revealed = False

    def unflag(self):
        self.flagged = False
    
    #coloca una mina
    def set_mine(self):
        self.mined = True
        self.set_value(-1)

    #cambia el valor de la casilla
    def set_value(self, value):
        self.value = value

    #devuelve si la casilla ha sido revelada o no
    def is_revealed(self):
        return self.revealed
    
    #devuelve si hay una mina en la casilla
    def is_mine(self):
        return self.mined

    #devuelve si hay una bandera en la casilla
    def is_flagged(self):
        return self.flagged

    #revela una casilla
    def box_reveal(self):
        # Si la casilla no está revelada
        if not self.is_revealed():
            self.reveal()
            # Si la casilla es un 0 revelo las cercanas
            if self.value == 0:
                self.reveal_neighbors(x, y)

    def reveal_neighbors(self):
        # Obtener la posición de la casilla dada
        x, y = self.x, self.y

        for i in range(-1, 1):
            for j in range(-1, 1):
                if x!=0 or y !=0:
                    neighbor_box = board[x+i][y+j]
                    if not neighbor_box.is_revealed():
                        neighbor_box.reveal()

