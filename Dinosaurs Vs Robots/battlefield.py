import robot
import dinosaur
from herd import Herd
from fleet import Fleet
import random


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    def run_game(self):  
        self.display_welcome()
        self.team = self.choose_team()
        self.battle()


    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs!')

        print('Each Robot and Dinosaur begin with 100 health.')
        print('Each character begins with 150 energy/power level points')
        print('and attacking requires 10 energy/power level points.')

        print('Robots belong to a Fleet and Dinosaurs belong to a Herd.')
        print('A winner is declared once all Robots in a fleet or ')
        print('all Dinosaurs in a Herd have 0 health.')


    def choose_team(self):
        choose_team = int(input('Choose your team: (1) Robots; (2) Dinosaurs'))
        if choose_team == 1:
            print('You chose the fleet of Robots')
            return choose_team
        elif choose_team == 2:
            print('You chose the herd of Dinosaurs')
            return choose_team
        else:
            print('Invalid answer. Try again.')
            self.choose_team()


    def battle(self):
        first_turn = random.randint(1, 2)
        if first_turn == 1:
            print('Robots are up first')
            first_turn = 1
        if first_turn == 2:
            print('Dinosaurs are up first')
            first_turn = 2


        if first_turn == 1:
            while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
                    if self.fleet.robots[0].health > 0 or self.herd.dinosaurs[0].health > 0:

                        self.robo_turn()  # First turn team

                        if self.herd.dinosaurs[0].health <= 0:
                            print(f'{self.herd.dinosaurs[0].type} is out.')
                            self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                        elif self.fleet.robots[0].health <= 0:
                            print(f'{self.fleet.robots[0].name} is out.')
                            self.fleet.robots.remove(self.fleet.robots[0])

                        if len(self.fleet.robots) == 0:
                            self.display_winners_dinosaurs()
                            return
                        elif len(self.herd.dinosaurs) == 0:
                            self.display_winners_robots()
                            return

                        self.dino_turn() 

                        if self.herd.dinosaurs[0].health <= 0:
                            print(f'{self.herd.dinosaurs[0].type} is out.')
                            self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                        elif self.fleet.robots[0].health <= 0:
                            print(f'{self.fleet.robots[0].name} is out.')
                            self.fleet.robots.remove(self.fleet.robots[0])

                        if len(self.fleet.robots) == 0:
                            self.display_winners_dinosaurs()
                            return
                        elif len(self.herd.dinosaurs) == 0:
                            self.display_winners_robots()
                            return


        elif first_turn == 2:
            while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
                    if self.fleet.robots[0].health > 0 or self.herd.dinosaurs[0].health > 0:

                        self.dino_turn() 

                        if self.herd.dinosaurs[0].health <= 0:
                            print(f'{self.herd.dinosaurs[0].type} is out.')
                            self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                        elif self.fleet.robots[0].health <= 0:
                            print(f'{self.fleet.robots[0].name} is out.')
                            self.fleet.robots.remove(self.fleet.robots[0])

                        if len(self.fleet.robots) == 0:
                            self.display_winners_dinosaurs()
                            return
                        elif len(self.herd.dinosaurs) == 0:
                            self.display_winners_robots()
                            return

                        self.robo_turn() 

                        if self.herd.dinosaurs[0].health <= 0:
                            print(f'{self.herd.dinosaurs[0].type} is out.')
                            self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                        elif self.fleet.robots[0].health <= 0:
                            print(f'{self.fleet.robots[0].name} is out.')
                            self.fleet.robots.remove(self.fleet.robots[0])

                        if len(self.fleet.robots) == 0:
                            self.display_winners_dinosaurs()
                            return
                        elif len(self.herd.dinosaurs) == 0:
                            self.display_winners_robots()
                            return


    def dino_turn(self):
        self.show_dino_opponent_options()
        self.herd.dinosaurs[0].attack_robot(self.fleet.robots[0])


    def robo_turn(self):
        self.show_robo_opponent_options()
        self.fleet.robots[0].attack_dinosaur(self.herd.dinosaurs[0])


 


    def show_dino_opponent_options(self):
        i = 1
        for element in self.fleet.robots:
            print(f'{element.name} has {element.health} health.')
            i += 1


    def show_robo_opponent_options(self):
        i = 1
        for element in self.herd.dinosaurs:
            print(f'{element.type} has {element.health} health.')
            i += 1


    def display_winners_robots(self):
       

        if self.team == 1:
            print("Beep Boop! The Robot fleet has defeated the herd of Dinosaurs win. You win!")
        if self.team == 2:
            print("Beep Boop! The Robot fleet has defeated the herd of Dinosaurs win. You lose.")
        

    def display_winners_dinosaurs(self):
       
        if self.team == 2:
            print("Rawr! The herd of Dinosaurs has defeated the fleet of Robots. You win!")
        if self.team == 1:
            print("Rawr! The herd of Dinosaurs has defeated the fleet of Robots. You lose.")
       
   