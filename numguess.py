import random

answer = random.randint(1, 100)
guess = int(input('Enter Your Guess!: '))

if answer == guess: 
  print('Congratulations')
