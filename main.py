from art import logo
import random

game_end = False
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
#checks if the user can go again
def can_guess():
  global remaining_guess
  if remaining_guess > 0:
    print("Guess again.")
  else:
    print("You've run out of guesses, You lose.")

"""body of game compares the user guess to answer, until no guesses remaining"""
def play_game():
  global remaining_guess
  global game_end
  print(f"You have {remaining_guess} attempts remaining to guess the number. ")
    # ask user for guess and check it with answer  
  user_guess = int(input("Make a guess: "))
  #check the user guess with answer return too low or too high
  if user_guess > answer:
    remaining_guess -= 1
    print("Too high. ")
    can_guess()
  elif user_guess < answer:
    remaining_guess -= 1
    print("Too low.")
    can_guess()
  else: 
    print(f"You got it! The answer was {answer}. ")
    remaining_guess = 0
    game_end = True

while remaining_guess > 0:
  play_game()