import random

def play_game():
    # Set the range for the magic number
    min_number = 1
    max_number = 100
    magic_number = random.randint(min_number, max_number)

    print("Welcome to the Magic Number Game!")
    print(f"I'm thinking of a number between {min_number} and {max_number}.")
    print("Can you guess the magic number?")

    guess = None
    num_attempts = 0
    attempt_limit = 10

    while guess != magic_number and num_attempts < attempt_limit:
        try:
            guess = int(input("Enter your guess: "))
            num_attempts += 1

            if guess < magic_number:
                print("Too low! Try a higher number.")
            elif guess > magic_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You've found the magic number in {num_attempts} attempts.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again == "yes":
        play_game()
    else:
        print("Thank you for playing the Magic Number Game!")

play_game()