from typing import ClassVar


class Hero:
    #private class variable 
    __jumlah = 0;
    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1
        
    #pakai getter method ini hanya berlaku utk object
    def getJumlah(self):
        return Hero.__jumlah
        
    # Method ini tidak berlaku utk object tapi berlaku utk flash 
    def getJumlah1():
        return Hero.__jumlah
    
    # method static (decorator) nempel ke object dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    
    # polymorphism dianggap sebagai kelas juga dan object juga
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

sniper = Hero('sniper')
print(Hero.getJumlah2())
sonar = Hero('sonar')
print(sniper.getJumlah2())
ajas = Hero('ajas')
print(Hero.getJumlah3()) #/ pakai ini juga bisa print(sniper.getJumlah3()) 
# print(Hero.__jumlah) error
# print(sniper.getJumlah())

# print(Hero.getJumlah())
