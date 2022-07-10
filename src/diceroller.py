import random

def main():
    print("[*] Dice Roller")
    sides, rolls = dieIntake()
    results = dieRoll(sides, rolls)
    print(prettifyResults(results))

def dieIntake():
    """Asks the user for the number of sides and rolls."""
    while 1:
        try:
            sides = int(input("[*] How many sides? "))
            rolls = int(input("[*] How many rolls? "))
            return sides, rolls
        except ValueError:
            print("[-] Not a number - please enter a correct value.")

def dieRoll(s, r):
    """Runs the simulation of the die with the values provided by the user."""
    print("\n[+] Rolling...")
    results = [0] * s
    for i in range(r):
        results[random.randrange(s)] += 1
    return results

def prettifyResults(a):
    """Prettifies the results, makes it easier to read."""
    string = "[*] Results:"
    for i, n in enumerate(a, 1):
        string += "\n[*] {0}: {1}".format(i,n)
    return string
