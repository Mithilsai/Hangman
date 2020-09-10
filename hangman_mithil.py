import random
from tqdm import trange # for animation
from time import sleep # for sleep

word_list = ['apple', 'pineapple', 'banana', 'mosambi',
         'strawberry', 'guava', 'blueberry', 'watermelon',
         'kiwi', 'mango', 'pomegranate', 'orange']
def get_word():
    word = random.choice(word_list)
    return word.upper()
    #changung to upper case letter


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    chance = 0
    print("\n\tHere we go")
    print("\n\tHint: Names of fruits")
    sleep(3)
    print(display_hangman(tries))
    print("\n\t\t", word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("\n\tGuess a single letter or an entire word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("\n\tYou already guessed the letter", guess)
            elif guess not in word:
                print("\n\t"+guess+"is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("\n\tWell done,", guess, "is in the word!")
                chance += 1
                # for every 3 correct tries will get a bonus try
                if chance == 3 and tries < 6:
                    tries += 1
                #pushing the guess letter into guessed_letters
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                # The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("\n\tYou already guessed the word", guess)
            elif guess != word:
                print("\n\t"+guess+"is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("\n\tNot a valid guess.")
        print(display_hangman(tries))
        print("\n\t\t", word_completion)
        print("\n")
    if guessed:
        sleep(2)
        print("\n\tCongratulations, you have guessed the word! You win!")
    else:
        sleep(2)
        print("\n\tOpps, you ran out of tries. The word was " + word + ". Try your luck again :)")


def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def main():
    print("\n\t")
    print("The Hangman".center(100, '*'))
    print("\n\tKindly, choose \n\t\t1.Start the game \n\t\t2.End the game")
    x = input("\n\tEnter your choice in Numeric Format: ")
    if int(x) == 1:
        for i in trange(15, desc="Loading", unit="data", unit_scale=1000, ascii=False):
            sleep(0.1)
        word = get_word()
        play(word)
        while input("\n\tDo you wish to play Again? (Y/N): ").upper() == "Y":
            word = get_word()
            play(word)
        print("Created by Mithil".center(100, '-'))
    elif int(x) == 2:
        print("\n\tHope to see you soon :)")
    else:
        print("\n\tI can't get you try again")

if __name__ == "__main__":
    main()

