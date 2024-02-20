import random
random.randint(1,100)
62
jackpot = random.randint(1,100)

guess = int(input("guess the number"))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess higher")
    else:
        print("Guess lower")
        
    guess = int(input("guess the number"))
    counter+=1
    
    
print("Right answer")
print("You took",counter,"attempts")
    