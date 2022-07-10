# import the time module + winsound
import time, winsound
  
# define the countdown func.
def countdown(t):
    print("[*] Countdown started.")
    while t:
        # print the remaining time
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("[+]", timer, end="\r")
        time.sleep(1)
        t -= 1
    duration = 1000  # milliseconds
    freq = 440  # Hz
    # beep sound
    winsound.Beep(freq, duration)
    print("[*] We're finished.")
  
  
def main():
    print("[*] Countdown")
    while 1:
        try:
            t = int(input("[*] Enter the countdown time in seconds: "))
            countdown(t)
        except ValueError:
            print("[-] Please enter a valid number.")
        else:
            break
        



  
