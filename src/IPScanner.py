from socket import *
import time

# port scanning using socket on python
# calculates overall time to get the ports

startTime = time.time()

def main():
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target) # get host by IP
    print ('Starting scan on host: ', t_IP) # scan
   
    for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      
      conn = s.connect_ex((t_IP, i)) # TCP scan
      if(conn == 0):
            print ('Port %d: OPEN' % (i,))
      s.close()

    print('Time taken:', time.time() - startTime)


