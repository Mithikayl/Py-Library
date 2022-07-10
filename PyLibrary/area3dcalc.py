import math

def main():
    print("[*] 3D Area Calculator")
    print("[*] 1. Cube")
    print("[*] 2. Sphere")
    print("[*] 3. Cone")
    print("[*] 4. Cylinder")
    print("[*] 5. Pyramid")
    print("[*] 6. Prism")
    shape = input("\n[*] Enter the shape: ")
    if shape == "cube":
        side = float(input("[*] Enter the side: "))
        print("[+] Calculating...")
        print("[*] The area is", cube_area(side))
    elif shape == "sphere":
        radius = float(input("[*] Enter the radius: "))
        print("[+] Calculating...")
        print("[*] The area is", sphere_area(radius))
    elif shape == "cone":
        radius = float(input("[*] Enter the radius: "))
        height = float(input("[*] Enter the height: "))
        print("[+] Calculating...")
        print("[*] The area is", cone_area(radius, height))
    elif shape == "cylinder":
        radius = float(input("[*] Enter the radius: "))
        height = float(input("[*] Enter the height: "))
        print("[+] Calculating...")
        print("[*] The area is", cylinder_area(radius, height))
    elif shape == "pyramid":
        base = float(input("[*] Enter the base: "))
        height = float(input("[*] Enter the height: "))
        print("[+] Calculating...")
        print("[*] The area is", pyramid_area(base, height))
    elif shape == "prism":
        base = float(input("[*] Enter the base: "))
        height = float(input("[*] Enter the height: "))
        length = float(input("[*] Enter the length: "))
        print("[+] Calculating...")
        print("[*] The area is", prism_area(base, height, length))
    else:
        print("[-] Unknown shape")

def cube_area(side):
    return 6 * side ** 2

def sphere_area(radius):
    return 4 * math.pi * radius ** 2

def cone_area(radius, height):
    return math.pi * radius ** 2 + math.pi * radius * height

def cylinder_area(radius, height):
    return 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height

def pyramid_area(base, height):
    return base * height / 3

def prism_area(base, height, length):
    return 2 * base * height + 2 * length * height

