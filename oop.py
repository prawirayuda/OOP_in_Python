# constructor
class Hero:
    def __init__(self,inputName, inputPower, inputArmor):
        self.name = inputName
        self.power = inputPower
        self.armor = inputArmor
        # print("he", x)

hero1 = Hero("sniper",12,1)
print(hero1.name)
print(hero1.power)
print(hero1.armor)
print(hero1.__dict__)# ini untuk menampilkan lengkap isi list nya

# hero2 = Hero()