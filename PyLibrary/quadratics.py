import math

def main():
    print("[*] Quadratic Equation Solver")
    print("[*] This solver uses the form ax^2 + bx + c = 0")
    a, b, c = input_num() # assign vars via input funct
    x1, x2 = quadratic(a, b, c) # calculate x1, x2
    print("[*] Value of x1 =", x1) # print x1
    print("[*] Value of x2 =", x2) # print x2

def input_num():
    a = int(input("[*] Enter a: "))
    b = int(input("[*] Enter b: "))
    c = int(input("[*] Enter c: "))
    return a, b, c

def quadratic(a, b, c):
    print("[+] Calculating...")
    # calculate the discriminant
    d = (b**2) - (4*a*c) 
    # return the two solutions
    while 1:
        try:
            return (-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a) # quadratic formula
        except ValueError:
            print("[!] Invalid equation")
            exit()
        except ZeroDivisionError:
            print("[!] Invalid equation")
            exit()
        else:
            break



