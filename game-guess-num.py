# prototype # by https://github.com/hellmak
import random

num_max     = 100
num_random  = num_max + 1
num_input   = 0
score       = 0

print("Number input only or you will break the game.")

while num_random != num_input:
    if num_random == num_max + 1:
        num_random = random.randrange(1,num_max)
    
    #cheats
    if num_input == 666:
        print("https://youtu.be/WxnN05vOuSM")
    if num_input == 1337:
        print(f"cheat {num_random}")
    if num_input == 1338:
        print("u r winrar!")
        score = 1
        break
    
    if 1 <= num_input <= num_max:
        if num_input < num_random:
            print("guess a higher number!")
        elif num_input > num_random:
            print("guess a smaller number!")
        
    

    num_input = int(input(f"Guess a number 1-{num_max}: "))
    
    score += 1

if score == 1:
    print("First guess, wow!")
else:
    print(f"You guessed the right number in {score} guesses!")
