# class Hero:
#     def __init__(self,name,health):
#         self.name = name
#         self.health = health
        
# class Hero_intel(Hero):
#     def __init__(self,name):
#         self.name = name
#         self.health = 200
# class Hero_strength(Hero):
#     def __init__(self,name):
#         self.name = name
#         self.health = 200
        
# lina = Hero_intel('agung')
# axe = Hero_strength('ugang')

# print(lina.name,"", lina.health)
# print(axe.name,"", axe.health)

class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
    def showInfo(self):
        print("{} dengan health: {}".format(self.name,self.health))
        
class Hero_1(Hero):
    def __init__(self,name):
        # Hero.__init__(self,name,100)
        super().__init__(name,100)
        super().showInfo()
        
class Hero_2(Hero):
    def __init__(self,name):
        # Hero.__init__(self,name,200)
        super().__init__(name,200)
        super().showInfo()
        
yud = Hero_1('yud')
da = Hero_2('da')
# print(yud.name, yud.health)
# print(da.name, da.health)