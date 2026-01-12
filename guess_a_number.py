from random import randint
computer_number = randint(1, 100)
while True:
    player_input = input("Guess a number between 1 and 100: ")
    if not player_input.isdigit():
        print("Please enter a number")
        continue
    else:
        trying_number = int(player_input)
        if computer_number == trying_number:
            print("You guessed the number")
            break
        elif trying_number > computer_number:
            print("Too high")
        elif trying_number < computer_number:
            print("Too low")
