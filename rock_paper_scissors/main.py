import random

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

while True:
    exit_the_game = input("Would you like to continue the game? type 'Y' or 'N': ").lower()
    if exit_the_game == "y":
        def play():
            users_choice = input("What do you choose? Type 'r' for Rock, 'p' for Paper or 's' for Scissors: ").lower()
            if users_choice == 'r':
                print(rock)
            elif users_choice == 's':
                print(scissors)
            elif users_choice == 'p':
                print(paper)
            computers_choice = random.choice(['r', 'p', 's'])
            if computers_choice == 'r':
                print(rock)
            elif computers_choice == 's':
                print(scissors)
            elif computers_choice == 'p':
                print(paper)

            # r > s, s > p, p > r

            if users_choice == computers_choice:
                return "It's a draw!"

            if win(users_choice, computers_choice):
                return "You win!"
            else:
                return "Oh no! You lose :( "


        def win(user, computer):
            if (user == "r" and computer == "s") or (user == "s" and computer == "p") or (
                    user == "p" and computer == "r"):
                return True


    elif exit_the_game == 'n':
        break

    print(play())
