import random

def role_power():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    dice4 = random.randint(1,6)
    dice_list = [dice1, dice2, dice3, dice4]
    dice_list.sort()
    dice_list.pop(0)
    return dice_list[0]+dice_list[1]+dice_list[2]

class npc():
    def __init__(self):
        self.force = role_power()
        self.agility = role_power()
        self.constitution = role_power()
        self.intelligence = role_power()
        self.sagesse = role_power()
        self.charisme = role_power()
        self.armor = random.randint(1, 12)
        self.name = "zoro"
        self.race = "swordman"
        self.kind = "santoryu"
        self.hp = random.randint(1,20)
        self.profession = "frontline"
    def show_stats(self):
        print(str(self.force))
        print(str(self.agility))
        print(str(self.constitution))
        print(str(self.intelligence))
        print(str(self.sagesse))
        print(str(self.charisme))
        print(str(self.armor))
        print(str(self.name))
        print(str(self.race))
        print(str(self.kind))
        print(str(self.hp))
        print(str(self.profession))

class kobold():
    def __init__(self):
        super().__init__()
    def attack(self, target):
        pass
    def dmg_taken(self, dmg):
        self.hp -= dmg

class hero(npc):
    def __init__(self):
        super().__init__()
    def attack(self, target):
        attack = random.randint(1,20)
        if attack == 20:
            strenght = random.randint(1,8)
            target.dmg_taken(strenght)
        elif attack > 1:
            if attack > target.armor:
                strenght = random.randint(1,6)
                target.dmg_taken(strenght)
    def dmg_taken(self, dmg):
        pass
