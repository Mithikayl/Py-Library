import PyLibrary
from PyLibrary import *

moduleList = []
for name in PyLibrary.__all__:
    module = locals()[name]
    moduleList.append(module)

def main():
    print("[*] Pick a module to use:\n")
    for i in range(len(moduleList)):
        print(str(i+1) + ": " + moduleList[i].__name__.replace("PyLibrary.", ""))
    item = int(input("\n[*] Enter a number:\n"))
    for i in range(len(moduleList)):
        if item == i+1:
            print("\n[*] " + moduleList[i].__name__.replace("PyLibrary.", "") + " selected\n")
            moduleList[i].main()
            break

if __name__ == "__main__":
    main()