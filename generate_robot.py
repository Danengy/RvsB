
from generate_weapon import Weapon

class Robot:

    def __init__(self, robot_name, robot_health ):
        self.robot_name = robot_name
        self.robot_health = robot_health
        self.active_weapon = Weapon("Rockets", 250)
    
    def attack_dino(self, dinosaur):
        dinosaur.dino_health -= self.active_weapon.weapon_attack_power
        return dinosaur


        

    