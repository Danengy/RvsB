print("Hello")
from generate_dino import Dinosaur
from generate_robot import Robot

t_rex = Dinosaur("Trex", 1000, 200)
alpha = Robot("Alpha", 1000)



            

class Battlefield:

    
    def __init__(self):
        pass
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):

        print("Welcome to Robot Vs Dinosaur! Get ready for a great battle!")
        print(f"\nWatch as the robot, {alpha.robot_name} fights against his opponent, The {t_rex.dino_name} ")

    def battle_phase(self):

        while (t_rex.dino_health >= 0 & alpha.robot_health >= 0):
                    print(f"Robot's current health: {alpha.robot_health}")
                    print(f"Dinosaur's current health: {t_rex.dino_health}")

                    print(f"\n{alpha.robot_name} attacks {t_rex.dino_name} with {alpha.active_weapon.weapon_name} dealing {alpha.active_weapon.weapon_attack_power}\n")
                    alpha.attack_dino(t_rex)
                    # print(f"The {t_rex.dino_name} current health is {t_rex.dino_health}")
                    print(f"The {t_rex.dino_name} attacks {alpha.robot_name} dealing {t_rex.dino_attack_power}\n")
                    t_rex.attack_robot(alpha)

                    if t_rex.dino_health ==0:
                        print(f"Robot's current health: {alpha.robot_health}")
                        print(f"Dinosaur's current health: {t_rex.dino_health}")
                        break
                    elif alpha.robot_health == 0:
                        print(f"Robot's current health: {alpha.robot_health}")
                        print(f"Dinosaur's current health: {t_rex.dino_health}")
                        break


    def display_winner(self):
        if t_rex.dino_health ==0:
            print(f"The Robot: {alpha.robot_name} WINS!!")
        elif alpha.robot_health == 0:
            print(f"The Dinosaur: {t_rex.dino_name} WINS!!")