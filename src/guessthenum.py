import random, essentials
global tries
tries = 0
essentials.clear()
thenum = random.randint(0, 100) # get random int
def guess(thenum, tries):
    if 2 > tries:
        if thenum < 50:
            print("Hint: Less than 50.")
        elif thenum == 50:
            print("Neither above or below 50.") # instant win, i guess. get lucky.
        else:
            print("Hint: Above 50.")
    elif tries == 2:
        print(f"Hint: Number is between {thenum - random.randint(-1, -20)} and {thenum +  random.randint(1, 20)}.")
    elif tries == 3:
        print(f"Hint: Number is between {thenum - random.randint(-1, -10)} and {thenum + random.randint(1, 10)}.")    
    elif tries >= 4:
        print(f"Hint: Number is between {thenum - random.randint(-1, -5)} and {thenum + random.randint(1, 5)}.")
    while essentials.guessnumguessed == False: # had to import var from essentials, otherwise would overwrite local var
        try:
            attempt = int(input('Guess a number between 1 - 100. '))
        except:
            exit("Not a number. Exiting program.")
        else:
            if attempt != thenum:
                print("Not quite. Try again.")
                tries = tries + 1
                guess(thenum, tries)
                guessed = False
                essentials.clear()
            elif attempt == thenum:
                finalscore = 3000 - (tries * 250)
                print(f"Bullseye. Your score was {finalscore} and you took {tries} tries.")
                essentials.guessnumguessed = True
guess(thenum, tries)
