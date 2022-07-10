import requests

def main():
    print("[*] Dad Joke Generator")
    print(get_joke())

def get_joke():
    print("[+] Fetching joke...")
    url = 'https://icanhazdadjoke.com/'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['joke']

