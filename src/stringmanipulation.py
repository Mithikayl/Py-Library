import random, time, os

def main():
    """A program which can manipulate strings"""
    # first we take strings from the user
    inputString = input('What string do you want to manipulate?\n')
    print(f'Your string is "{inputString}"') # tell the user their string
    maniType = chooseMani()
    prettifyResults(manipulation(maniType, inputString))
    

class stringEditing:
    def __init__(self, string):
        """Initialises the class with the string specified"""
        self.string = string

    
    def getVowels(self):
        """Function that grabs all vowels in a strings"""
        vowels = 'aeiou'
        list = [v for v in self.string if v in vowels]
        return ''.join(list)   
    
    def randomiseString(self):
        """Randomises the string using random module"""
        return ''.join(random.choice(self.string) for i in range(len(self.string))) 

    def listifyString(self):
        """String manipulation 101"""
        list = [letter for letter in self.string] # iterate through string into lists
        return list
    
    def getConsonants(self):
        """Function that grabs all cosonants in a strings"""
        consonants = 'bcdfghjklmnpqrstvwxyz'
        list = [v for v in self.string if v in consonants]
        return ''.join(list)   

def chooseMani():
    print(f'What kind of manipulation do you want? Reply with the number you want.\n1. String to List\n2. Randomise string letters\n3. Pick out all vowels from string.\n4. Get consonants from string')
    while True:
        try:
            maniChoice = int(input()) # check if it is an int
            if maniChoice > 4: # check if it is an option within our range
                raise ValueError # raise error if not
            else:
                break
        except ValueError:
            print("That's not a choice.")
            continue
    return maniChoice

def manipulation(choice, string):
    manipulateString = stringEditing(string)
    if choice == 1:
        print("You have chosen to make the string into a list.")
        time.sleep(2)
        return manipulateString.listifyString()
    elif choice == 2:
        print("You have chosen to randomise the string.")
        time.sleep(2)
        return manipulateString.randomiseString()
    elif choice == 3:
        print("You have chosen to get the vowels in the string.")
        time.sleep(2)
        return manipulateString.getVowels()
    elif choice == 4:
        print("You have chosen to get the consonants in the string.")
        time.sleep(2)
        return manipulateString.getConsonants()        
    

def prettifyResults(result):
    print(f'The result of your manipulation is:\n{result}') # prettify results

if __name__ == "__main__":
    os.system('cls')
    main()

