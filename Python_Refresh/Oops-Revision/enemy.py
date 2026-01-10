import random
class Enemy:
    health : int 
    attack: int
    type_of_enemy: str

    def __init__(self,type_of_enemy,attack=1,health=10):
        self.__type_of_enemy=type_of_enemy
        self.attack=attack
        self.health=health

        print(f"HI {self.get_type_of_enemy()} is your enemy with health {self.health} and attack")

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def set_type_of_enemy(self,enemy_type:str):
        self.__type_of_enemy=enemy_type
        return self.__type_of_enemy

    def talk(self):
        print(f"I am a {self.__type_of_enemy} !! Be prepared to fight")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} is moving closer to you")

    def attack_by_enemy(self):
        print(f'{self.get_type_of_enemy()} is coming and will acttack you for the point {self.attack}')

    def special_attack(self):
        print("Enemy has no special Attack")
    


class Zombie(Enemy):
    def __init__(self, type_of_enemy="Zombie", attack=1, health=10):
        super().__init__( type_of_enemy,attack, health)

    def talk(self): #(Method Overridining)
        print(f"{self.get_type_of_enemy()} Is here to Spread infection")

    def special_attack(self):
        did_special_attack_work=random.random()<0.50
        if did_special_attack_work:
            print("Zombie Regenrated !!!!!>>>>+2 HP")
            self.health+=2
        




class Chudail(Enemy):
    def __init__(self,type_of_enemy="Chudail",attack=1,health=10):
        super().__init__(type_of_enemy,attack,health)

    def talk(self):
        print(f"{self.get_type_of_enemy()} is there to finish you !!!")
    
    def special_attack(self):
        did_special_attack_work=random.random()<0.20
        if did_special_attack_work:
            print("Chudail Gets Angry and get the increase the attack damage by 4")
            self.attack+=4