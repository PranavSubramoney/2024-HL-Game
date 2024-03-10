import random
import math


# Function to generate a secret number
def generate_secret_number(low, high):
    return random.randint(low, high)


# Function to calculate the score based on the guess and the secret number
def calculate_score(guesses_used, max_guesses):
    if guesses_used == 1:
        return 10
    elif guesses_used == 2:
        return 5
    elif guesses_used == 3:
        return 3
    else:
        return 1


# Main routine starts here

def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes or no")


def instructions():
    print('''
 **** Instructions ****
To begin choose the number of rounds you want to play or press enter for 
infinite mode. If you choose infinite mode, you'll play until you decide to stop.

Guessing the Secret Number:
Once the game starts, you'll be given a range of numbers to guess from.
You'll make guesses by entering a number within the specified range.
After each guess, the game will provide feedback, letting you know if your guess is too high or too low.
If you're close to running out of guesses, the game will warn you to be careful.

If you guess the secret number within the allowed number of guesses, you win the round.
If you run out of guesses before guessing the correct number, you lose the round.
You can also choose to end the round by typing "xxx" if you need to quit.

Point system:
Win in 1 guess = 10 points
Win in 2 guesses = 5 points
Win in 3 guesses = 3 points
Win in 4 or more guesses = 1 points

Have fun and good luck!
    ''')


def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response
        try:
            response = int(response)
            if low is not None and response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


def main():
    print("🔼🔼🔼 Welcome to Higher Lower Game 🔻🔻🔻")
    print()
    want_instructions = yes_no("Do you want to read the instructions? (Enter yes or no) ")
    if want_instructions == "yes":
        instructions()

    mode = "regular"
    rounds_played = 0
    end_game = "no"
    feedback = ""
    game_history = []
    all_scores = []

    num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ",
                           low=1, exit_code="")

    if num_rounds == "":
        mode = "infinite"
        num_rounds = 5

    default_params = yes_no("Do you want to use the default game parameters? ")
    if default_params == "yes":
        low_num = 0
        high_num = 10
    else:
        low_num = int_check("Low Number? ")
        high_num = int_check("High Number? ", low=low_num + 1)

    guesses_allowed = calc_guesses(low_num, high_num)

    while rounds_played < num_rounds:
        if mode == "infinite":
            rounds_heading = f"\n♾♾♾ Round {rounds_played + 1} of (Infinite Mode) ♾♾♾"
        else:
            rounds_heading = f"\n🕒🕒🕒 Round {rounds_played + 1} of {num_rounds} 🕒🕒🕒"
        print(rounds_heading)
        print()
        guesses_used = 0
        already_guessed = []
        secret = generate_secret_number(low_num, high_num)
        guess = ""
        while guess != secret and guesses_used < guesses_allowed:
            guess = input("Guess: ").lower()
            if guess == "xxx":
                print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔.")
                end_game = "yes"
                break
            try:
                guess = int(guess)
            except ValueError:
                print("Please enter a valid number.")
                continue
            if guess < low_num or guess > high_num:
                print("Please enter a number within the valid range.")
                continue
            if guess in already_guessed:
                print(f"You've already guessed {guess}. You've *still* used "
                      f"{guesses_used} / {guesses_allowed} guesses ")
                continue
            else:
                already_guessed.append(guess)
            guesses_used += 1
            if guess < secret and guesses_used < guesses_allowed:
                feedback = (f"Too low, please try a higher number. "
                            f"You've used {guesses_used} / {guesses_allowed} guesses")
            elif guess > secret and guesses_used < guesses_allowed:
                feedback = (f"Too high, please try a lower number. "
                            f"You've used {guesses_used} / {guesses_allowed} guesses")
            elif guess == secret:
                if guesses_used == 1:
                    feedback = "🍀🍀 Lucky! You got it on the first guess. 🍀🍀"
                elif guesses_used == guesses_allowed:
                    feedback = f"Phew! You got it in {guesses_used} guesses."
                else:
                    feedback = f"Well done! You guessed the secret number in {guesses_used} guesses."
            else:
                feedback = "Sorry - you have no more guesses. You lose this round!"
            print(feedback)
            if guesses_used == guesses_allowed - 1 and guess != secret:
                print("\n💣💣💣 Careful - you have one guess left! 💣💣💣\n")
        print()
        print("End of round")
        if end_game == "yes":
            break
        rounds_played += 1
        if mode == "infinite":
            num_rounds += 1
        score = calculate_score(guesses_used, guesses_allowed)
        game_history.append(score)
        print(f"Points scored in this round: {score}")

    # Display game history if user wants to see it
    print()
    show_history = yes_no("Do you want to see the game history? ")
    if show_history == "yes":
        print("\n🏆🏆🏆 Game History 🏆🏆🏆")

        for round_num, score in enumerate(game_history, start=1):
            print(f"Round {round_num}: {score} points")

    print("\n\n📊📊📊 Game Statistics 📊📊📊")

    if len(game_history) == 0:
        print("No rounds played yet.")
    else:
        best_score = max(game_history)
        worst_score = min(game_history)
        total_score = sum(game_history)
        average_score = total_score / len(game_history)

        print(f"Best Score: {best_score} points")
        print(f"Worst Score: {worst_score} points")
        print(f"Total Score: {total_score} points")
        print(f"Average Score: {average_score:.2f} points")

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
