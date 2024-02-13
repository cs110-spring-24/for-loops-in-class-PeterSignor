import random 
one = 0 
two = 0
three = 0 
four = 0
five = 0 
sixes = 0 
for rolls in range(100):
    dice = random.randint(1,6)
    if dice == 1:
        print ("1")
        one += 1 
    elif dice == 2:
        print ("2")
        two += 1 
    elif dice == 3:
        print ("3")
        three += 1    
    elif dice == 4:
        print ("4")
        four += 1 
    elif dice == 5:
        print ("5")
        five += 1         
    else:
        print ("6")
        sixes += 1 
print(f"You rolled {one} 1's, {two} 2's, {three} 3's, {four} 4's, {five} 5's, {sixes} 6's")