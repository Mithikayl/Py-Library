import random, essentials

def main():
    essentials.clear()
    print("*** DICE ROLLER ***")
    print("Enter q on first prompt to exit program.")
    while 1:
        sides = input(f'\nHow many sides? ')
        if sides == 'q':
            return
        try:
            sides = int(sides)
            rolls = int(input("How many rolls? "))
            print(prettifyResults(dieRoll(sides, rolls)))
        except ValueError:
            print("Not a number - please enter a correct value.")

def dieRoll(s, r):
    """Runs the simulation of the die with the values provided by the user."""
    results = [0] * s
    for i in range(r):
        results[random.randrange(s)] += 1
    return results

def prettifyResults(a):
    """Prettifies the results, makes it easier to read."""
    string = "Results:"
    for i, n in enumerate(a, 1):
        string += "\n{0}: {1}.".format(i,n)
    return string

if __name__ == '__main__':
    main()