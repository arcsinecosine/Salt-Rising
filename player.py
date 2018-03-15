class player():
    def __init__(self,type):
        if (type == 1):  #
            self.HP = 10  #Base HP
            self.SKP = 5  #Base Skill Stamina
            self.STR = 5  #Base Strength
            self.SKS = 5  #Base Skill Strength
            self.XP = 0   #Base XP
            self.BTC = 10 #
            self.LVL = 1

    def level_up(self):

        