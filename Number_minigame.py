import random

print("Hello! This is a number guessing game.")
print("I will choose a number between 1 and 100, and you have to guess it.")
print("Every time you guess, I will tell you if your guess is too high or too low.")
pc_number = random.randint (1, 100)

difficulty = input("Choose a difficulty level (easy, medium, hard): ").strip().lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "medium":
    attempts = 7
elif difficulty == "hard":
    attempts = 5
else:
    print("Invalid difficulty level. Defaulting to easy mode.")
    attempts = 10

print(f"You have {attempts} attempts to guess the number.")
for attempt in range(attempts):
    print(f"Attempt {attempt + 1} of {attempts}.")
    if attempt == attempts - 1:
        print("This is your last attempt!")
    print("Make your guess:")
    try:
        user_guess = int(input())
        if user_guess < 1 or user_guess > 100:
            print("Please guess a number between 1 and 100.")
            continue
        
        if user_guess < pc_number:
            print("Your guess is too low.")
        elif user_guess > pc_number + 10:
            print("Your guess is way too high!")
        elif user_guess < pc_number - 10:
            print("Your guess is way too low!")
        elif user_guess > pc_number:
            print("Your guess is too high.")
        else:
            print("Congratulations! You've guessed the number!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 100.")
if user_guess != pc_number:
    print(f"Sorry, you've used all your attempts. The number was {pc_number}. Better luck next time!")