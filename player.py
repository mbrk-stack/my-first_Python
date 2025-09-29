class Player:
    def __init__(self):
        self.energie = 3
        self.alive = True
        
    def blessure(self):
        if self.alive:
            self.energie -= 1
            if self.energie <= 0:
                self.energie = 0
                self.alive = False
    
    def __str__(self):
        return f"{self}."
    
    def soin(self):
        if self.alive:
            self.energie += 1
        else:
            print('Vous ètes mort')
            

player1 = Player()
# print(player1.energie, player1.alive)

# player1.blessure()
# player1.blessure()
# player1.soin()
# player1.blessure()
# # player1.blessure()
# player1.soin()

# print(player1.energie, player1.alive)

print(player1)
