class Hero:
    jumlah_hero = 0
    def __init__(self,inputName,inputHealth,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.armor = inputArmor
        Hero.jumlah_hero += 1
        
        
    def siapa(self):
        print("namaku"+ self.name)
    
hero1 = Hero("sniper",12,12)
hero2 = Hero("aga",1,1)

print(hero1.__dict__)
print(hero2.__dict__)