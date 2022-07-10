import math

def main():
    print("[*] Area Calculator")
    print("[*] 1. Rectangle")
    print("[*] 2. Triangle")
    print("[*] 3. Circle")
    print("[*] 4. Trapezium")
    print("[*] 5. Parallelogram")
    shape = input("\n[*] Enter the shape: ")
    if shape == "rectangle":
        width = float(input("[*] Enter the width: "))
        height = float(input("[*] Enter the height: "))
        print("[+] Calculating...")
        print("[*] The area is", rectangle_area(width, height))
    elif shape == "triangle":
        base = float(input("[*] Enter the base: "))
        height = float(input("[*] Enter the height: "))
        print("[+] Calculating...")
        print("[*] The area is", triangle_area(base, height))
    elif shape == "circle":
        radius = float(input("[*] Enter the radius: "))
        print("[+] Calculating...")
        print("[*] The area is", circle_area(radius))
    elif shape == "trapezium":
        base1 = float(input("[*] Enter the base 1: "))
        base2 = float(input("[*] Enter the base 2: "))
        height = float(input("[*] Enter the height: "))
        print("[+] Calculating...")
        print("[*] The area is", trapezium_area(base1, base2, height))
    elif shape == "parallelogram":
        base = float(input("[*] Enter the base: "))
        height = float(input("[*] Enter the height: "))
        print("[+] Calculating...")
        print("[*] The area is", parallelogram_area(base, height))
    else:
        print("[-] Unknown shape")

def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return base * height / 2

def circle_area(radius):
    return math.pi * radius ** 2

def trapezium_area(base1, base2, height):
    return (base1 + base2) * height / 2

def parallelogram_area(base, height):
    return base * height

