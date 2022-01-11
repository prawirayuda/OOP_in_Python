class Hero:
    def __init__(self, name, health, armor): 
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth: {}".format(self.__name,self.__health)
        # self.info = "name {} : \n\thealth: {}".format(self.__name,self.__health)
        
    # def gethealth(self):
    #     return self.__health
    
    @property
    #merubah sebuah method menjadi sebuah variable
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name,self.__health)

    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, input):
        self.__armor = input
        
        
    @armor.deleter
    def armor(self):
        print('armor didelete')
        self.__armor = None

sniper = Hero('sniper', 100,10)
# print(sniper.gethealth())
print(sniper.info)
sniper.name = 'sayah'
print(sniper.info)
# sniper.info = "ok"
# print(sniper.info) 
print(sniper.__dict__)

print('getter dan setter untuk __armor: ')
print(sniper.armor)
# sniper.armor = 18


# sniper.armor(50)
sniper.armor= 50
print(sniper.armor)
print(sniper.__dict__)


#delete armor 
print("delete armor")
del sniper.armor
print(sniper.__dict__)

#encapulasi dengan cara python