#buat semua variable private lalu utk mengambil data yg dibutuh kan kita pakai getter dan setter
#geeter utk mengambil variable
#setter utk mensetting variable
class Hero:
    def __init__(self,name,health,attack):
        self.__name = name
        self.__health = health
        self.__power = attack
    #getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health
    
    #setter
    def diserang(self,serangPower):
        self.__health -= serangPower
        

eater = Hero("eater", 90,2)

print(eater.__dict__)        
# print(eater.__name) #kalau ambil data pakai ini maka tidak bisa maka nya diperlukan dengan getter like in below
print(eater.getName())


print(eater.getHealth())
eater.diserang(5)
print(eater.getHealth())