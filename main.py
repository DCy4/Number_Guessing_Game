from art import logo
import random

remaining_guess = 0
#game start
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1,100)
#test random number
print(f"Pssst, the correct answer is {answer} ")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")

if difficulty == 'easy':
  remaining_guess = 10
else: 
  remaining_guess = 5
  
print(f"You have {remaining_guess} attempts remaining to guess the number. ")
# ask user for guess and check it with answer  
