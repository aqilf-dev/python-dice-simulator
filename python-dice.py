# Dice

def dice():
    import random
    import time as t


    while True:


        print("Welcome to python dice! (press anywhere to continue and press 'x' to stop the program)")

        user_continue_input = input(">> ").lower()

        if user_continue_input == "x":
            print("Goodbye!")
            break

        try:
            minimum_range = int(input("Input Minimum Number: "))
            maximum_range = int(input("Input Maximum Number: "))

            if maximum_range < minimum_range:
                print("Maximum number cannot be less than minimum number")
                continue
            dice_range = random.randint(minimum_range, maximum_range)

            print(f"\nDICE RANGE SET! ({minimum_range} to {maximum_range})")

            while True:
                random_dice_rolling_time = random.randint(2, 4)
                user_roll_input = input("Press ENTER to roll dice, press 'n' to reset range, and press 'x' to exit program\n").lower()
                if user_roll_input == 'n':
                    break
                elif user_roll_input == 'x':
                    print("Goodbye!")
                    exit()
                else:
                    print("Rolling Dice..")
                    t.sleep(random_dice_rolling_time)
                    print(f"Dice is showing.. {dice_range}")
                    continue


        except ValueError:
            print("Please input numbers only\n")

if __name__ == "__main__":
    dice()