secret_number = 9
guess_count = 0
guess_limit = 3

playername = input("Enter your name:")
print(f" Hello, {playername}. Guess the magic number between 1 and 10!")



while guess_count < guess_limit:
    guess = float(input("Enter your guess: "))
    guess_count += 1
    if guess != secret_number and guess_count!=3:
        print("\n" f"Incorrect, You have {guess_limit - guess_count} guesses remaining")
    elif guess == secret_number:
        print("\n" f"Correct. Congratuations.....{playername}, though we have reason to believe you cheated.")
    elif guess_count == guess_limit:
        print("\n" f"I'm sorry {playername}, You are all out of guesses. You are Mayor of Loserville :( ")

print(input("\n" "Press Enter to close"))
