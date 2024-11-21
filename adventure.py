import time

# Function to add a delay between messages
def print_pause(message, delay=2):
    print(message)
    time.sleep(delay)

# Function to introduce the game
def intro():
    print_pause("You find yourself standing in a dark forest.")
    print_pause("Rumor has it that a fierce dragon guards a hidden treasure.")
    print_pause("Your mission is to find the treasure and defeat the dragon!")
    print_pause("You see two paths ahead of you.")
    print_pause("One leads to a dark cave, and the other leads to a village.")

# Function to present choices
def choose_path():
    print("\nWhich path do you want to take?")
    print("1. The dark cave")
    print("2. The village")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        dark_cave()
    elif choice == "2":
        village()
    else:
        print_pause("Invalid choice. Please try again.")
        choose_path()

# Function for the dark cave path
def dark_cave():
    print_pause("\nYou walk into the dark cave.")
    print_pause("It's damp, and you can hear the faint growl of the dragon.")
    print_pause("You see a shiny sword stuck in a rock!")
    print("\nWhat will you do?")
    print("1. Take the sword.")
    print("2. Leave the cave.")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print_pause("\nYou pull the sword out of the rock. It glows with magical energy!")
        print_pause("With newfound courage, you confront the dragon!")
        dragon_battle(sword=True)
    elif choice == "2":
        print_pause("\nYou leave the cave, unarmed but alive.")
        choose_path()
    else:
        print_pause("Invalid choice. Please try again.")
        dark_cave()

# Function for the village path
def village():
    print_pause("\nYou arrive at the village and meet an old wise man.")
    print_pause("He warns you about the dragon and offers you a shield.")
    print("\nWhat will you do?")
    print("1. Take the shield.")
    print("2. Politely decline and leave.")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print_pause("\nYou take the shield and thank the wise man.")
        print_pause("Armed with the shield, you feel more prepared.")
        dragon_battle(shield=True)
    elif choice == "2":
        print_pause("\nYou leave the village and return to the forest.")
        choose_path()
    else:
        print_pause("Invalid choice. Please try again.")
        village()

# Function for the dragon battle
def dragon_battle(sword=False, shield=False):
    print_pause("\nYou find yourself face-to-face with the fierce dragon!")
    if sword and shield:
        print_pause("With the glowing sword and shield, you defeat the dragon easily!")
        print_pause("You claim the hidden treasure and emerge as a hero!")
    elif sword:
        print_pause("With the glowing sword, you charge at the dragon.")
        print_pause("The dragon breathes fire, but your courage prevails!")
        print_pause("You slay the dragon and claim the treasure!")
    elif shield:
        print_pause("You bravely defend yourself with the shield.")
        print_pause("However, without a weapon, you cannot defeat the dragon.")
        print_pause("The dragon chases you away. Better luck next time!")
    else:
        print_pause("Unarmed and unprotected, you have no chance against the dragon.")
        print_pause("You run away and live to fight another day.")
    print_pause("\nGAME OVER")

# Main function to start the game
def play_game():
    intro()
    choose_path()

# Start the game
if __name__ == "__main__":
    play_game()
