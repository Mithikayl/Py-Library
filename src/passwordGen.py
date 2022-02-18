import time, random, string

def main():
    """A python script to build strong passwords"""
    print("Welcome to the PyPassGen.")
    lengthOfPass = charLength()
    genPass = generator(lengthOfPass)
    time.sleep(1)
    prettifyResults(lengthOfPass, genPass)
    pass

def charLength():
    """User specifies character length for password"""
    while 1:
        try:
            length = int(input("How long do you want the password to be? NOTE: Under 20 and over 8 is best.\n"))
        except ValueError:
            print("That's not an option.")
            continue
        else:
            return length


def generator(charLength):
    """Generates a secure password using character length as a basis"""
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation) for _ in range(charLength))

def prettifyResults(length, genPass):
    print("Your generated password with {} character length is:".format(length))
    time.sleep(2)
    print(genPass)

if __name__ == "__main__":
    main()