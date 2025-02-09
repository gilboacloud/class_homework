# get input of only positive numbers
import math
x=1
num_list = []
y = int(input(f'please enter number #{x}:' ))
while True:
    if y>0 :
        num_list.append(y)
        x+=1
        y = int(input(f'please enter number #{x} avg={sum(num_list)/len(num_list)} sum= {sum(num_list)}: ' ))
    else:
        print("you enterted a negative number - bye")
        break