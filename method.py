#intraksi antar object dan interaksi antar class

class Hero:
    jumlah_hero= 0
    
    def __init__(self,input_name,input_health,input_armor):
        #instance variable
        self.name = input_name
        self.health = input_health
        self.armor = input_armor
        Hero.jumlah_hero +=1

    # void function, method tanpa return
    def siapa(self):
        print("namaku adalah "+ self.name)
    
    #method dengan argument tanpa return
    def healthup(self,up):
        self.health += up
        
    #method dengan return
    def getHealth(self):
        return self.health

                
hero1 = Hero('sniper', 100,10)
hero2 = Hero('agung', 1,10)
hero3 = Hero('hait', 100,1)



hero1.siapa()
hero1.healthup(10)
# print(hero1.health)
print(hero1.getHealth())

# print(hero1.__dict__)
# print(hero2.__dict__)




""" 
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

 """