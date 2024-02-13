import random
heads = 0
tails = 0
for flip in range(100):
    coin = random.randint(1,2)
    if coin == 1:
        print("Heads")
        heads += 1 
    else: 
        print ("tails")
        tails += 1   
print (f"After 100 flips, we flipper {heads} heads and {tails} tails")	   
