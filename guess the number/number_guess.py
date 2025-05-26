from art import logo
import random
print(logo)

GUESSED_NUMBER = random.randint(1, 100)

def game_proper():
    lives = 0
    print("Yo! guess my number. (It's between 1 and 100 btw)")
    # I know this undermines the guessing part just pls it's for my testing so ignore it lol
    print(f"Just to hook ya up, ima say it to you in secret. It's {GUESSED_NUMBER}")

    difficulty = input("What's your difficulty? Easy or Hard? \n").lower()
    if difficulty == "easy":
        lives += 10
    else:
        lives += 5

    while lives != 0:
        user_guess = int(input("Make a guess: "))

        if user_guess == GUESSED_NUMBER:
            print("YOO THAT'S RIGHT", "YOU WIN")
            lives = 0
        elif user_guess != GUESSED_NUMBER:
            if user_guess > GUESSED_NUMBER:
                print("Too high brah")
            elif user_guess < GUESSED_NUMBER:
                print("Too low brah")

            lives -= 1
            print(f"You have {lives} attempts left man.")

        if lives == 0:
            print(f"The number was {GUESSED_NUMBER}")

game_proper()