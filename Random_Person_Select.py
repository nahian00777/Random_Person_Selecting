from random import randint, random
from time import sleep
person_num = input("How many person you want:")
person_num = int(person_num)
l1 = []
random_value = randint(1,person_num)
for i in range(1,person_num+1):
    person_name = input(f"Enter {i}th name:")
    l1.append(person_name)
    
for i in range(1,person_num+1):
    if(random_value == i):
        sum = i;
        break
print("Selecting the winner....")
sleep(2)   
print(l1[sum-1] + " is the winner!!!")

input("Press Enter to exit!")
           