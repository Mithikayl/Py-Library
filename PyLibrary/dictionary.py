import requests

def main():
    print("[*] Dictionary")
    word = input("[*] Enter a word: \n")
    reachApi(word)

def reachApi(word):
    print("[+] Fetching...")
    r = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word))
    # response
    if r.status_code == 200:
        # data gathered
        data = r.json()
        # print definition
        for i in data:
            print("\n[*] Word: {}".format(i["word"]))
            print("[*] Definition: {}".format(i['meanings'][0]['definitions'][0]['definition']))
            print("[*] Synonyms: {}".format(i['meanings'][0]['definitions'][0]['synonyms']))
            print("[*] Antonyms: {}".format(i['meanings'][0]['definitions'][0]['antonyms']))
    else:
        # error
        print("[-] Word not found")
        
