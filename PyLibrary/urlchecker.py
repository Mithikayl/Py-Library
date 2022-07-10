import time, sys
from urllib.request import urlopen
from urllib.error import HTTPError
def main():
    print("[*] URL Checker")
    urls = urlIntake()
    results = urlChecking(urls)
    displayResults(urls, results)
    pass

def urlIntake():
    print("[*] Enter how many URLs to test.")
    while True:
        try:
            urlCount = int(input())
        except ValueError:
            print("[-] Not a valid number.")
            continue
        else:
            break
    urllist = []
    for i in range(urlCount):
        url = input("[*] URL: ")
        urllist.append(url)
    return urllist

def urlChecking(urllist):
    resultList = []
    for i in urllist:
        try:
            urlopen(i)
        except HTTPError:
            resultList.append()
        except:
            resultList.append(0)
        else:
            resultList.append(1)
    return resultList

def displayResults(urllist, resultlist):
    fullResults = []
    for i in resultlist:
        if i == 0:
            fullResults.append("[!] Unavailable")
        if i == 1:
            fullResults.append("[*] Available")
    print("\n[*] RESULTS\n----------------------------------------")
    time.sleep(2)
    for(i, x) in zip(urllist, fullResults):
        print(f"[*] URL: {i}, Status: {x}")
        time.sleep(1)

