from datetime import date, datetime

def main():
    print("[*] Clock")
    # assign vars
    today = date.today()
    now = datetime.now()

    # more vars
    datetoday = today.strftime("%B %d, %Y.") # -> placeholders for values
    currenttime = now.strftime("%H:%M:%S.")
    # print using vars
    print("[*] Today is", datetoday)
    print("[*] The time currently is", currenttime)
