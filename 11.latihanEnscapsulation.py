class Hero:
     #private class variabel 
    __jumlah = 0;
    
    def __init__(self,name,health,power,armor):
        self.__name = name
        self.__healthbase = health
        self.__powerbase = power
        self.__armorbase = armor
        self.__level = 1
        self.__exp = 0
        
        self.__healthMax = self.__healthbase * self.__level
        self.__power =self.__powerbase * self.__level
        self.__armor = self.__armorbase * self.__level
        
        self.__health = self.__healthMax
        
        
        Hero.__jumlah += 1
        
    @property
    def info(self):
        return " {} level {}: \n\thealth = {}/{}\n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__power,self.__armor)
    
    @property
    def gainExp(self):
        pass


    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100
                    
            self.__healthMax = self.__healthbase * self.__level
            self.__power =self.__powerbase * self.__level
            self.__armor = self.__armorbase * self.__level
            
    def attack(self,musuh):
        self.gainExp = 50
    
    
slader = Hero('slader', 100,5,10)
sonar = Hero('sonar', 100,5,10)
print(slader.info)

# slader.gainExp = 50
# slader.gainExp = 80
slader.attack(sonar)
slader.attack(sonar)
slader.attack(sonar)
print(slader.__dict__)
print(slader.gainExp)