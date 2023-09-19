import random
from termcolor import cprint , colored
exe_list=["Biecep Curl" , "Push ups " , "Situp", "Leg Raise" , "Back Row","Tri exe","kick back", "Chest fly" , "Hammer Curl" , "Squat" , "Lungs" , "clave raises" , "Chest press" , "Skull crunshes " , "Shoulder press " , "Latteral raise" , "Plank" , "Reverse plank"]



choice = random.choice(exe_list)


cprint(f"The exe for today is {choice}", "white" , "on_green")

