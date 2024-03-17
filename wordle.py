# User input their guess
secret_word = "ERUPT"
counter = 1

while counter < 7:
    print(f"GUESS {counter}")
    user_guess = input("Guess the secret word: ").upper()
    if user_guess == secret_word:
        print("Congratulation you guessed the secret word!")
    else:
        user_guess_list = list(user_guess)
        correct_letter = []
        incorrect_letter = []
        for letter in user_guess_list:
            # Need to fix this part for repeated letters in user_guess
            if letter in secret_word:
                correct_letter.append(letter)
            else:
                incorrect_letter.append(letter)
        print("Wrong guess.\n"
              f"Correct letters: {correct_letter}\n"
              f"incorrect_letters: {incorrect_letter}\n")
        if counter == 6:
            print("Game over, you have used up all your tries.\n"
                  f"The secret word was {secret_word}")
    counter += 1
