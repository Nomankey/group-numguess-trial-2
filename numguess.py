import random


answer = random.randint(1, 100)
guess = int(input('Enter Your Guess!: '))

if answer == guess: 
    print('Congratulations')
elif answer > guess:         # Add elif -> if answer == guess가 아닐 때'Up'을 print! 
   print('Up!')           
