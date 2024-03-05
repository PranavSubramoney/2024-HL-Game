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


# checks for integer more than 0 (allows <enter>
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


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

print("program continues")

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5


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