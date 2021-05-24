import random

word_list = ['python', 'java', 'kotlin', 'javascript']

print("H A N G M A N")

while True:
    word = random.choice(word_list)
    guessed_word = "-" * len(word)
    input_letter = ""
    remaining_letters = word
    typed_letters = [""]
    lives = 8
    choice = input("Type 'play' to play the game, 'exit' to quit: ").lower()
    if choice == "exit":
        break
    elif choice == "play":
        print("\n" + guessed_word)

        while lives > 0:
            input_letter = input("Input a letter: ")

            if len(input_letter) != 1:
                print("You should input a single letter")
            elif input_letter in typed_letters:
                print("You already typed this letter")
            elif not input_letter.islower():
                print("It is not an ASCII lowercase letter")
            elif input_letter in remaining_letters:
                remaining_letters = remaining_letters.replace(input_letter, "")
                guessed_word = word
                for letter in remaining_letters:
                    guessed_word = guessed_word.replace(letter, "-")
            else:
                print("No such letter in the word")
                lives = lives - 1
            if lives > 0:
                print("\n" + guessed_word)
            if guessed_word == word:
                print("You guessed the word!\nYou survived!\n")
                break
            if lives == 0:
                print("You are hanged!\n")

            typed_letters.append(input_letter)
    else:
        continue
