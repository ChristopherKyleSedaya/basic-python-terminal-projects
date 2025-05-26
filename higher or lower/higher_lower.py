from game_data import data
import art
import random

print(art.logo)


game_running = True

higher = []


score = 0
while game_running:
    if score == 0:
        a = random.choice(data)
        b = random.choice(data)
    elif a == b:
        b = random.choice(data)

    hold = b

    if score >= 1:
        a = hold
        b = random.choice(data)
    elif a == b:
        b = random.choice(data)

    print(f"Your current score: {score}")
    print(f"A{a['follower_count']} B{b['follower_count']} ")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_guess == "A" and a['follower_count'] > b['follower_count']:
        score += 1
        print("\n" *100)

    elif user_guess == "B" and a['follower_count'] < b['follower_count']:
        score += 1
        print("\n" * 100)
    else:
        print(f"sorry that's wrong. Final score {score}")
        game_running = False
