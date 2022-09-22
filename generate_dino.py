class Dinosaur:

    def __init__(self, dino_name, dino_health, attack_power):
        self.dino_name = dino_name 
        self.dino_health = dino_health
        self.dino_attack_power = attack_power
    
    def attack_robot(self, robot):
        robot.robot_health -= self.dino_attack_power 
        return robot 
        

        

        




    

         