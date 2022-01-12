class Hero:
    def __init__(self,name):
        self.health_pool = [0,100,200,300,400,500]
        self.power_pool = [0,10,20,30,40,50] 
        self.armor_pool = [0,1,2,3,4,50]
        
        self.__name = name
        self.__exp = 0
        self.__exp = 0
        self.__level = 0
        
    def show_info(self):
        print(f"level {self.__level}")
        # # print("{}\n\tlevel : {}\n\thealth : {} \n\tpower: {}\n\tarmor : {}".format(
        #     self.__name,
        #     self.__level,
        #     self.__health,
        #     self.__power,
        #     self.__armor
        # # ))      
        
    @property
    def health_pool(self):
        pass
    @property
    def power_pool(self):
        pass
    @property
    def armor_pool(self):
        pass
    @property
    def level(self):
        pass
    @property
    def gainExp(self):
        pass
    
    @health_pool.setter
    def health_pool(self,input):
        self.__health_pool = input

    @power_pool.setter
    def power_pool(self,input):
        self.__power_pool = input

    @armor_pool.setter
    def armor_pool(self,input):
        self.__armor_pool = input
    
    @gainExp.setter
    def gainExp(self,input):
        self.__exp += input
        if(self.__exp >= 100):
            self.level = self.__exp//100
            self.__exp %= 100
            
    @level.setter
    def level(self,input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__power = self.__power_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]
    
    
class Hero1(Hero):
    def __init__(self,name):
        super().__init__(name)
        self.health_pool =[0,50,100,150,200,250]
        self.power_pool = [0,20,30,60,80,100]
        self.armor_pool = [0,1,2,3,4,5]
        self.level= 1
class Hero2(Hero):
    def __init__(self,name):
        super().__init__(name)
        self.health_pool =[0,50,100,150,200,250]
        self.power_pool = [0,20,30,60,80,100]
        self.armor_pool = [0,1,2,3,4,5]
        self.level= 1
        

lina = Hero1('lina')
slader = Hero2('slader')

lina.show_info()
