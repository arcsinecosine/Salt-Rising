class player():
    def __init__(self,type):
        if (type == 1):  # Karl Marx Class
            self.HP = 10  #Base HP
            self.SKP = 5  #Base Skill Stamina
            self.STR = 5  #Base Strength
            self.SKS = 5  #Base Skill Strength
            self.XP = 0   #Base XP
            self.BTC = 10 #Base amount of bitcoin
            self.LVL = 1
            self.CRIT = None
            self.BTC_RATIO = 0.75
        elif (type == 2): #Trump Class
            pass
        elif (type == 3): #Elon Musk Class
            pass
        elif (type == 4): #Zucc Class
            pass

    def level_up(self):
        print ("You have leveled up!")
        print ("Please select a stat to increase!")
        