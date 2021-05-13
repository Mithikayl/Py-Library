import random, essentials
def roll():
    essentials.clear()
    num1 = input("What number should be the minimum? ")
    num2 = input("What number should be the maximum? ")
    try: # try this
        diceroll = random.randint(int(num1), int(num2)) 
    except: # if dont work
        print("Not a number.")
    else: # if do work
        return print(f"You rolled a {diceroll}.")
roll()
choice = input("Roll again? (Y/N) ")
if choice.lower() == "y":
    roll()
else:
    exit("Exiting program.")
