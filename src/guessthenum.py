import random, essentials

def main():
    essentials.clear()
    print("** GUESS THE NUMBER GAME ***")
    print("A number between 1 and 100 will be generated. \nThe less tries you get it in, the better.")
    print(scoreCalculator(guessTheNumber()))
    
def guessTheNumber():
    number = random.randint(1, 100)
    tries = []
    while 1:
        try:
            guess = int(input("Guess the number: "))
            if guess == number:
                tryCount = len(tries)
                print("You guessed the number in {} tries!".format(tryCount))
                return tryCount
            else:
                raise TypeError()
        except ValueError:
            print(f"Numbers only, please.")
        except TypeError:
            print("Wrong! Try again. \nHint: it's between {} and {}!".format(number - random.randint(5, 10), number + random.randint(5, 10)))
            tries.append(1)

def scoreCalculator(a):
    overallScore = 3000 - (a * 250)
    return "Your overall score was {}".format(overallScore)

if __name__=='__main__':
    main()
