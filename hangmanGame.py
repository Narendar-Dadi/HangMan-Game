#HANGMAN GAME
from wordLetter import words
import random




hangman_art = {0: ("   ",
                                   "   ",
                                   "   "),
                             1: (" o ",
                                   "   ",
                                   "   "),
                             2: (" o ",
                                   " | ",
                                   "   "),
                             3: (" o ",
                                   "/| ",
                                   "   "),
                             4: (" o ",
                                  "/|\\",
                                   "   "),
                              5: (" o ",
                                   "/|\\",
                                   "/  "),
                              6: (" o ",
                                   "/|\\",
                                   "/ \\")}


def display_man(wrong_guess):
    for line in hangman_art[wrong_guess]:
        print(line)
    print("***************")


def display_hint(hint):
        print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guess=0
    guessed_letters=set()
    is_runinig=True

    while is_runinig:

        display_man(wrong_guess)
        display_hint(hint)

        guess=input("Enter your Guess : ").lower()

        if len(guess)  !=1 or not guess.isalpha():
            print("Invalid input")
            continue


        if guess.isdigit():
            print("Invalid Input")
            continue


        if guess in guessed_letters:
            print(f"{guess} is already Guessed ")
            continue
        guessed_letters.add(guess)


        if guess in answer:
           for i in range(len(answer)):
               if answer[i] ==guess:
                   hint[i]=guess
        else:
            wrong_guess+=1

        if "_" not in hint:
            display_man(wrong_guess)
            display_answer(answer)

            print(" 🎉 YOU WIN 🌟 ")
            is_runinig=False
        elif wrong_guess>=len(hangman_art)-1:
            display_man(wrong_guess)
            display_answer(answer)
            print("YOU LOST 😓!")
            is_runinig=False

if __name__=='__main__':
    main()