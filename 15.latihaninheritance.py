from hero import Hero1,Hero2

lina = Hero1('lina')
slader = Hero2('slader')

lina.show_info()
slader.show_info()

lina.gainExp = 200
slader.gainExp = 100
lina.show_info()
slader.show_info()