class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
    def showInfo(self):
        print("showInfo di class Hero")
        print("{} health: {}".format(self.name,self.health))
        
class Hero_1(Hero):
    def __init__(self,name):
        super().__init__(name,100)
    
    #ovveride show info
    def showInfo(self):
        print("ini show info di class hero 1")
        print("{}\n\t Tipe:Hero1,\n\thealth: {}".format(self.name,self.health))
        
class Hero_2(Hero):
    def __init__(self,name):
        super().__init__(name,200)
    
lina = Hero_1('lina')
sarah = Hero_2('sarah')
# lina.showInfo()
sarah.showInfo()