import os

def main():
    print("[*] Filesystem")
    dir = getdir()
    thing(dir)
    pass

def getdir():
    directory = input("[*] Enter the directory (leave empty for current):\n")
    return directory

def thing(dir): # if no filesystem argument is passed, print home directory
    if dir == None:
        path = os.path.join(os.path.expanduser('~'), '')
        print("[*]", os.listdir(path))
    # if filesystem argument is passed, print filesystem
    else:
        path = os.path.join(os.path.expanduser('~'), dir)
        print("[*]", os.listdir(path))