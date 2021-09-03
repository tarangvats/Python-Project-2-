#Number Guessing Game Objectives:
from art import logo
# Include an ASCII art logo.
print(logo)
# Allow the player to submit a guess for a number between 1 and 100.
import random
actual_number = random.randint(1,100)
print("I'm thinking of a number between 1 to 100. Can you find it?")
def guess():
  chosen_number = int(input("Make a guess: "))
  return chosen_number
levels = {"hard":5,"easy":10}
chosen_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
n = guess()
while n!=actual_number and levels[chosen_level]>0 :
  if n>actual_number:
    print("Too high.\n")
  else:
    print("Too low.\n")
  levels[chosen_level] = levels[chosen_level]-1
  if levels[chosen_level]==0:
    break
  print(f"Guess again.\n You have {levels[chosen_level]} attempts remaining to guess the number.\n") 
  n = guess() 
  
if n==actual_number:
  print("You WON!")
else:
  print("YOU LOSE!")  

