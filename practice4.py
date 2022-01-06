# def game(n):
#     return n
        
# n=int (input("enter the score of the game\n"))
# score=game(n)
# with open("score.txt","r") as f:
#         b=f.read()
# if b=='':
#     with open("score.txt","w")as f:
#         f.write(str(score))
# elif int(b)<score:
#       with open("score.txt","w")as f:
#         f.write(str(score))



# for i in range(1,21):
#     with open(f"multiplication{i}.txt","w") as f:
#         for j in range(1,11):
#             f.write(f"{i} X {j} = {i*j}\n")
#         break



# with open("censored.txt","r") as f:
#     context=f.read()
# if "ishwar"or"boko"in context:
#     context=context.replace("ishwar","#####")
#     context=context.replace("boko","$$$$$")
#     with open("censored.txt","w") as f:
#         f.write(context)


# with open("censored.txt","r") as f:
#     context=f.read()
# if "python" in context.lower():
#     print("yes pyhton is present")
# else:
#     print("sorry python is not present")

# from tqdm import tqdm
# from time import sleep
# for i in tqdm(range(100)):
#     sleep(0.1)
# import pyfiglet
# text="ok no problem"
# print(pyfiglet.figlet_format(text))

import pyfiglet
from termcolor import colored
text="i love coding"
print(colored(pyfiglet.figlet_format(text),'blue'))
