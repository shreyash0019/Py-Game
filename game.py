import random
def number_g_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("*"*50)
    print("I have chosen a number between 1 and 100. Try to guess it!")
    print("*"*50)
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
                print("*" * 50)
            elif guess > number_to_guess:
                print("Too high! Try again.")
                print("*" * 50)
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")


if __name__ == "__main__":
    number_g_game()
