import random


answer = random.randint(1, 100)
guess = int(input('Enter Your Guess!: '))

if answer == guess: 
    print('Congratulations')
elif answer > guess:          # if answer == guess가 아닐 경우'Up'을 출력 
   print('Up!')           
