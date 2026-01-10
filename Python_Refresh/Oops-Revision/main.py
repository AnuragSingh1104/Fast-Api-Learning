from enemy import Enemy
from enemy import Zombie
from enemy import Chudail
from hero import Hero
from weapon import Weapon


enemy1=Enemy("Bhoot",2,15)
enemy2=Enemy("Zombie")

# enemy1.type_of_enemy="Bhoot"

print(enemy1.health)
print(enemy2.health)


print('*'*60)

# Abstraction
enemy1.talk()

# print(f"Enemy {enemy1.type_of_enemy} has the health value of {enemy1.attack} which can do the damage of {enemy1.attack}")

enemy1.walk_forward()
enemy1.attack_by_enemy()

print('*'*60)

#Encapsulation - getting and setting the private variable through getter and setter
print(enemy1.get_type_of_enemy())

enemy1.set_type_of_enemy("chudail")
print(enemy1.get_type_of_enemy())


## Practicing Interitence
enemy2=Zombie()
print(enemy2.talk())


# Polymorphism

def battle(e1: Enemy,e2: Enemy):    
    e1.talk()
    e2.attack_by_enemy()
    while e1.health>0 and e2.health>0:
        print("-"*40)
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()} : {e1.health} HP Remain")
        print(f"{e2.get_type_of_enemy()} : {e2.health} HP Remain")

        print(f'{e1.get_type_of_enemy()} attacks for {e1.attack} damage')
        print(f'{e2.get_type_of_enemy()} attacks for {e2.attack} damage')

        e2.special_attack()
        e1.health-=e2.attack
        e1.special_attack()
        e2.health-=e1.attack

        print('-'*40)
    
    if e1.health>0:
        print(f'{e1.get_type_of_enemy()} Wins!')
    else:
        print(f'{e2.get_type_of_enemy()} Wins')

zombie=Zombie(attack=2,health=20)
chudail=Chudail(attack=3,health=20)

battle(zombie,chudail)


print('-'*60)
print('+'*60)



def hero_battle(hero: Hero,enemy: Enemy):    

    while hero.health_points>0 and enemy.health>0:
        print("-"*40)


        print(f'Heros : {hero.health_points} Hp Left')
        print(f'{enemy.get_type_of_enemy()} :{enemy.health} HP left')

        enemy.special_attack()
        hero.health_points-=enemy.attack
        hero.attack()
        enemy.health-=hero.attack_damage

        print('-'*40)
    
    if hero.health_points>0:
        print('Hero  Wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} Wins')

zombie=Zombie(attack=2,health=10)
heros=Hero(10,1)
weapons=Weapon('Sword',5)
heros.weapon=weapons
heros.equip_weapon()
hero_battle(hero=heros,enemy=zombie)






