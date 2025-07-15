import random

def play_game():
    print("Welcome to the Number Guessing Game!")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input(" Enter your guess (1-100): "))
        except ValueError:
            print(" Invalid input! Please enter a valid integer.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print(" Too low. Try again!")
        elif guess > number_to_guess:
            print(" Too high. Try again!")
        else:
            print(f" Correct! You guessed the number in {attempts} attempts.")
            break

    replay = input(" Do you want to play again? (yes/no): ").lower()
    if replay == "yes":
        play_game()
    else:
        print(" Thanks for playing!")

play_game()

