from urllib.request import urlopen
from urllib.error import HTTPError
import itertools, time
# CODE PLAN:
# structure so that we intake the urls into a list to be iterated through a check
# can interpret it into a dictionary but we can do that after
# after that compile url responses into its own list
# after this, display it in a topdown view. probably a table to show all results 

def main():
    urls = urlIntake()
    results = urlChecking(urls)
    displayResults(urls, results)
    pass

def urlIntake():
    print("Enter how many URLs to test.")
    while True:
        try:
            urlCount = int(input())
        except ValueError:
            print("Not a valid number.")
            continue
        else:
            break
    urllist = []
    for i in range(urlCount):
        url = input("URL: ")
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
            fullResults.append("Unavailable")
        if i == 1:
            fullResults.append("Available")
    print("\nRESULTS\n----------------------------------------")
    time.sleep(2)
    for(i, x) in zip(urllist, fullResults):
        print(f"URL: {i}, Status: {x}")
        time.sleep(1)

if __name__ == "__main__":
    main()