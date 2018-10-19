lottery_player = {"name" : "Rolf", "numbers" : (20,40,30,85)}
#print(lottery_player)

class Lottery_player:
    def __init__(self,name="Rolf",numbers=(20,40,30,85)):
        self.name = name
        self.numbers = numbers
    def total(self):
        return sum(self.numbers)

Player = Lottery_player("Nagesh",(12,24,36,48,60))
print(Player.name , Player.numbers)
print(Player.total())
