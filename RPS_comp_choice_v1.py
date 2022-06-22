# RPS Component 1 - generate computer choice

import random

rps_list = ["Rock", "Paper","Scissors"]

for item in range (0,20):
    comp_choice = random.choice(rps_list[:-1])
    print(comp_choice, end="\t")