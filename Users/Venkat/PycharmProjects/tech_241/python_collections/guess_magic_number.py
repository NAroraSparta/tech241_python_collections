#Here is some extremely basic Pseudocode to get you started (I recommend researching and using pseudocode often as it is very helpful):

# Magic number game

# Set magic number

# Ask the user for a guess

# Check if the user's guess was correct

# Give them the result

magic_number = 5
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess the magic number:  "))
    guess_count += 1
    if guess == magic_number:
        print("You won!")
        break
else:
    print("Better luck time!")

