import random
import math
import time
from termcolor import colored , cprint



x = 0

start_time = time.time()
end_time = start_time + 500

while x <= 10 :
    while time.time() < end_time:
        random.seed()
        rn = random.randint(100 , 999)
        S = rn * 11
        PS = int(input(f"Enter the solution of {rn} * 11 :"))
        if PS == S :
            cprint(f"The Answer is correct {rn} * 11 {S}", "white","on_green")
            scr += 1
        else :
            cprint(f"The Answer is incorrect {rn} * 11 = {S} " , "black" , "on_red")
    x += 1

cprint(f"Your Score for this game is {scr}" , "black" , "on_blue")
