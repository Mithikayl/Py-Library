import os, sys, essentials

def main():
    checkModules()
    pass

def checkModules():
    while 1:
        try:
            import requests
            from urllib.request import urlopen, HTTPError, URLError
        except ImportError:
            downloadModules = input("You do not have these modules. Would you like to download them? (Y/N)")
            if downloadModules.lower() == "y":
                os.system('pip install --user requests urllib3')
            else:
                return
        else:
            continue

def checkURL(url):
    try:
        urlopen(url)
        return True
    except HTTPError:
        return False
    except URLError:
        return False

if __name__ == '__main__':
    main()