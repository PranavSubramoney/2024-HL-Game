import math
import random


# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes or no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes or no")


def instructions():
    print('''

 **** Instructions ****



    ''')


# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the umber needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs tobe between low and high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response
        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# calculate the umber of guesses allowed
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

print("🔼🔼🔼 Welcome to Higher Lower Game 🔻🔻🔻")
print()

want_instructions = yes_no("Do you want to read the instructions? (Enter yes or no) ")

# checks users enter (y) or (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ",
                       low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# ask user if they want to customise the number range
default_params = yes_no("Do you want to use the default game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

# allow user to choose the high / low number
else:
    low_num = int_check("Low Number? ")
    high_num = int_check("High Number? ", low=low_num + 1)

# calculate the maximum number of guesses based on the low and high number
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Round headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾♾♾ Round {rounds_played + 1} of (Infinite Mode) ♾♾♾"
    else:
        rounds_heading = f"\n🕒🕒🕒 Round {rounds_played + 1} of {num_rounds} 🕒🕒🕒"

    print(rounds_heading)
    print()

    # Round starts here
    # Set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # Choose a 'secret' number between the low and high number
    secret = random.randint(low_num, high_num)

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # ask the user to guess the number...
        guess = input("Guess: ").lower()  # Modified to get user input as a string

        # check that they don't want to quit
        if guess == "xxx":
            print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔.")
            end_game = "yes"
            break

        # Convert the guess into an integer and proceed as before
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        # check that guess is within the valid range
        if guess < low_num or guess > high_num:
            print("Please enter a number within the valid range.")
            continue

        # check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You've already guessed {guess}. You've *still* used "
                  f"{guesses_used} / {guesses_allowed} guesses ")
            continue

        # if guess is not a duplicate, add it to the 'already guessed' list
        else:
            already_guessed.append(guess)

        # add one to the number of guesses used
        guesses_used += 1

        # compare the user's guess with the secret number set up feedback statement
        # (code for feedback remains unchanged)

        # If we have guesses left...
        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"Too low, please try a higher number. "
                        f"You've used {guesses_used} / {guesses_allowed} guesses")
        elif guess > secret and guesses_used < guesses_allowed:
            feedback = (f"Too high, please try a lower number. "
                        f"You've used {guesses_used} / {guesses_allowed} guesses")

        # when the secret number is guessed, we have three different feedback
        # options (lucky / 'phew' / well done)
        elif guess == secret:

            if guesses_used == 1:
                feedback = "🍀🍀 Lucky! You got it on the first guess. 🍀🍀"
            elif guesses_used == guesses_allowed:
                feedback = f"Phew! You got it in {guesses_used} guesses."
            else:
                feedback = f"Well done! You guessed the secret number in {guesses_used} guesses."

        # if there are no guesses left!
        else:
            feedback = "Sorry - you have no more guesses. You lose this round!"

        # print feedback to user
        print(feedback)

        # Additional Feedback (warn user that they are running out of guesses
        if guesses_used == guesses_allowed - 1:
            print("\n💣💣💣 Careful - you have one guess left! 💣💣💣\n")

    print()
    print("End of round")

    # Round ends here

    # if user has entered exit code, end game!
    if end_game == "yes":
        break

    rounds_played += 1


    # if users are in infinite mode , increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game History / Statistics area
