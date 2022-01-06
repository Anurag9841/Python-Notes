import random
from tqdm import tqdm
from time import sleep
import pyfiglet
from termcolor import colored
for i in tqdm(range(100)):
    sleep(0.01)
def game(comp,player):
    if comp=="S" and player=="W":
        print(colored(pyfiglet.figlet_format("Player you lose:"),'red'))
    elif comp=="W" and player=="S":
          print(colored(pyfiglet.figlet_format("Player you won:"),'blue'))
    elif comp=="G"and player=="S":
           print(colored(pyfiglet.figlet_format("Player you lose:"),'green'))
    elif comp=="S"and player=="G":
           print(colored(pyfiglet.figlet_format("Player you won:"),'yellow'))
    elif comp==player:
        print("You tied the match:")
    elif comp=="W" and player=="G":
          print(colored(pyfiglet.figlet_format("Player you lose:"),'blue'))
    else:
         print(colored(pyfiglet.figlet_format("Player you won:"),'yellow'))
randno=random.randint(1,3)
if randno==1:
    comp="S"
elif randno==2:
    comp="W"
else:
    comp="G"
player=input("select Snake(S),Water(W)and Gun(G)??\n")
print(f"Computer selected {comp}")
print(f"Player secected {player}")
game(comp,player)