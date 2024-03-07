import math


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

To begin, decide on a score goal (eg: First one to get a 
score of 50 wins). 

For each round of the game, you win points by rolling dice.
At the start of each round, the player and the computer each roll two dice
and thereafter one. 

The winner of the round is the first person who gets 13 points or less, you cannot go over 13.
If you go over 13 you lose the round and do not get any points.

If you win the round, your score will increase by the
number of points that you earned. If your first roll of two
dice is a double (eg:both dice show a six), then your score will be 
DOUBLE the number of points (2 6's = 12, 12 x 2 = 24 points)

If you and the computer tie (eg: you both get a score of 10),
then you will have 10 points added to your score.

Your goal is to get to the target score before the computer.

Good luck.

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

print("🔼🔼🔼 Welcome to Higher Lower Game 🔻🔻🔻")
print()

want_instructions = yes_no("Do you want to read the instructions? (Enter yes or no) ")

# checks users enter (y) or (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Get Game parameters
low_num = int_check("Low Number? ")
high_num = int_check("High Number? ", low=low_num + 1)
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Round headings
    if mode == "infinite":
        rounds_heading = f"\n♾♾♾ Round {rounds_played + 1} of (Infinite Mode) ♾♾♾"
    else:
        rounds_heading = f"\n🕒🕒🕒 Round {rounds_played + 1} of {num_rounds} 🕒🕒🕒"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = input("Choose: ")

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode , increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game History / Statistics area


# extra
# rounds = "test"
# while rounds != "":
#     rounds = int_check("Rounds <enter for infinite>: ", low=1, exit_code="")
#     print(f"You asked for {rounds}")


# low_num = int_check("Low Number? ")
# print(f"You chose a low number of {low_num}")

high_num = int_check("High Number? ", low=1)
print(f"You chose a high number of {high_num}")

# Check user progress
guess = ""
while guess != "xxx":
    guess = int_check("Guess: ", low=0, high=10, exit_code="xxx")
    print(f"You guessed {guess}")
    print()

# Main routine starts here
