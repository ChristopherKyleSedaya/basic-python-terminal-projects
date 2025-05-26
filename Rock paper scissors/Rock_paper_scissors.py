rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# user choice

input_user = input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n")
if input_user == "0":
    print(rock)
elif input_user == "1":
    print(paper)
elif input_user == "2":
    print(scissors)
else:
    print("wrong input")

# list for rock paper scissors
options_for_computer = [rock, paper, scissors]

#Computer choice

import random
random_picker = random.choice(options_for_computer)
print("Computer chose:")
print(random_picker)

#logic for result

if input_user == "0":
    if random_picker == options_for_computer[0]:
        print("Tied")
    elif  random_picker ==  options_for_computer[1] :
        print("You lose")
    elif  random_picker ==  options_for_computer[2]:
        print("You win")
    else:
        print("test")
elif input_user == "1":
    if  random_picker ==  options_for_computer[0]:
        print("You win")
    elif  random_picker ==  options_for_computer[1]:
        print("Tied")
    elif  random_picker ==  options_for_computer[2]:
        print("You lose")
    else:
        print("test")
elif input_user == "2":
    if  random_picker ==  options_for_computer[0]:
        print("You lose")
    elif  random_picker ==  options_for_computer[1]:
        print("You Win")
    elif random_picker ==  options_for_computer[2]:
        print("Tied")
    else:
        print("test")
else:
    print("Test")

