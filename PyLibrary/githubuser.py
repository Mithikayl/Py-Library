import requests
import json

def main():
    """
    Main function
    """
    print("[*] Github User")
    user = input("[*] Enter a github username: ")
    data = fetch_data(user)
    prettifyresults(data)

def fetch_data(user):
    print("[+] Fetching data...")
    url = 'https://api.github.com/users/' + user
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def prettifyresults(data):
    print("\n[*] Username:", data['login'])
    print("[*] Name:", data['name'])
    print("[*] Location:", data['location'])
    print("[*] Followers:", data['followers'])
    print("[*] Following:", data['following'])
    print("[*] Public Repos:", data['public_repos'])
    print("[*] Public Gists:", data['public_gists'])
    print("[*] HTML URL:", data['html_url'])
    print("[*] Blog:", data['blog'])
    print("[*] Company:", data['company'])
    print("[*] Email:", data['email'])
    print("[*] Bio:", data['bio'])
    print("[*] Hireable:", data['hireable'])
    print("[*] Created at:", data['created_at'])
    print("[*] Updated at:", data['updated_at'])

