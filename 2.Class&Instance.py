class Hero:
    #class variabel variabel kelas
    jumlah = 0
    def __init__(self,inputName):
        #instance variabel / attribut
        self.name = inputName
        Hero.jumlah+=1
        print("Membuat Hero dengan nama "+ inputName)
        
hero1 = Hero("Snop")
print(Hero.jumlah)
hero2 = Hero("Snop")
print(Hero.jumlah)
hero2 = Hero("Snop")
print(Hero.jumlah)