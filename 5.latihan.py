class Hero:
    def __init__(self,name,health,attack,armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        
    def serang(self,lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self,self.attack)
    
    def diserang(self,lawan,attackPower_lawan):
        print(self.name  + ' diserang ' + lawan.name)
        attack_diterima = attackPower_lawan / self.armor
        print('serangan terasa : ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))
        
sniper = Hero('sniper',100,1,1)
snr = Hero('snr',100,2,2)



sniper.serang(snr)
print("\n")
snr.serang(sniper)


