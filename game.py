


menu = """***Welcome to the Journey to Mount Qaf*** 

1- Press key '1' or type 'start' to start a new game
2- Press key '2' or type 'load' to load your progress
3- Press key '3' or type 'quit' to quit the game"""

def get_selection(*values):

        choice = input().lower()

        try:
            i = int(choice)
            if 1 <= i <= 3:
                return i
        except ValueError as e:
            if choice in values:
                return values.index(choice) + 1

        print("Unknown input! Please enter a valid one.")


def game():
    print(menu)
    choice = get_selection("start", "load", "quit")
    if choice == 1:
        print("Starting a new game...")
    elif choice == 2:
        print("No save data found!")

    print("Goodbye!")

    print()

game()
