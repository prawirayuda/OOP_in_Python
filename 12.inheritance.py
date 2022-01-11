#pewarisan / yg diturunkan 
class Hero :
    def __init__(self,name,health):
        self.name = name
        self.health = health

class Hero_intellegent(Hero):
    pass
class Hero_strength(Hero):
    pass

lina = Hero ('lina', 100)
tea = Hero_intellegent('tea',60)
b = Hero_strength('axe',20)
# print(lina.name)
# print(help(tea))
print(tea.__dict__)
print(tea.name)
print(tea.health)
print(b.name)