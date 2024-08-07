from words import word_list
from art import logo,stages
import random

chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
game = False
len_chosen_Word = len(chosen_word)
disp =[]
for i in range(len_chosen_Word):
    disp.append("_")
print(logo)


while not game:
    print(f"The Word is {''.join(disp)}")
    print(stages[lives])
    guess = input("guess the letter ").lower()
    if guess in disp:
        print("Already guessed")
    for i in range(len_chosen_Word):
        letter = chosen_word[i]
        if letter == guess:
          disp[i] = letter
    if guess not in disp:
        print("letter not present in word you loose a life ")
        lives-=1
        if lives==0:
            game=True
            print("You loose")

    if "_" not in disp:
        game =True
        print("You WOn !")