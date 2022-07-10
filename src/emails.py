def main():
    print("[*] Emails")
    email = input("[*] Enter an email address:\n")
    slicer(email)

def slicer(email):
    while 1:
        try:    
            username = email.split("@")[0]
            domain = email.split("@")[1]
        except IndexError:
            print("[-] Invalid email address")
            email = input("[*] Enter an email address:\n")
            continue
        else:
            break
    print("[*] Username: " + username)
    print("[*] Domain: " + domain)
    
