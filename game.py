


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

def user():
    choice = input("Enter a user name to save your progress or type '/b' to go back")

    if choice == "/b":
        print("Going back to menu...")
        return False
    else:
        user =  { "username" : choice , "characters": {}, "bag" : {}}

        print("Create your character:")
        characters = ["name","species","gender"]

        for i,character in enumerate(characters,1):
            user["characters"][character] = input(f"{i}-{character}")

        print("Pack your bag for the journey:")
        user["bag"]["snack"] = input("Favorite snack")
        user["bag"]["weapon"] = input("A weapon for the journey")
        user["bag"]["tool"] = input("A traversal tool")

        print("""Choose your difficulty:
1- Easy
2- Medium
3- Hard
""")
        difficulties= ["easy","medium","hard"]
        user["difficulty"] = get_selection(* difficulties)
        print("Good luck on your journey!")
        print("Your character: ", ", ".join(user["characters"].values()))
        print("Your inventory: ", ", ".join(user["bag"].values()))


        print("Difficulty :", difficulties[user["difficulty"] - 1])
        return True


def game():
    stop_game = False
    while not stop_game:
        print(menu)
        choice = get_selection("start", "load", "quit")
        if choice == 1:
            print("Starting a new game...")
            stop_game = user()
        elif choice == 2:
            print("No save data found!")
        else:
            break
    print("Goodbye!")

game()
