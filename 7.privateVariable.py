class Hero:
    #class variabel 
    jumlah = 0
    def __init__(self,nama,health):
        self.name = nama
        self.health = health 
        
        #membuat variable private
        self.__private = "private"
        
        #variable instance protected
        self._protected = "protected"
        
# lina = Hero("lina", 100) 
# print(lina.__dict__)
# print(lina.__private)
# print(lina.health)        

lina = Hero ("lina",100)

print(lina.__dict__)
print(lina._protected)

lina._protected ="testing"
print(lina.__dict__)
print(lina._protected)
